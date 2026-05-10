"""Utility functions for running agents on CLI."""
import asyncio
import signal
import re
from typing import Any, Optional, NoReturn, TypeAlias
import types as types_module

from google.adk import runners
from google.adk.agents import base_agent
from google.adk.artifacts import base_artifact_service
from google.adk.artifacts import in_memory_artifact_service
from google.adk.events import event as event_lib
from google.adk.memory import base_memory_service
from google.adk.memory import in_memory_memory_service
from google.adk.sessions import base_session_service
from google.adk.sessions import in_memory_session_service
from google.genai import types
try:
    import gnureadline as readline
except ImportError:
    import readline

from rich import console
import termcolor

from langunittest.utils import colored_logging as clog


Agent = base_agent.BaseAgent
BaseArtifactService: TypeAlias = base_artifact_service.BaseArtifactService
BaseSessionService: TypeAlias = base_session_service.BaseSessionService
BaseMemoryService: TypeAlias = base_memory_service.BaseMemoryService
Console = console.Console
Runner: TypeAlias = runners.Runner
REQUEST_CONFIRMATION_FUNCTION_CALL_NAME = 'adk_request_confirmation'


def _format_ask_user_confirmation_requests(
    function_calls: list[types.FunctionCall],
) -> str:
  """Formats a list of ask_user_confirmation function calls."""
  output = []
  for fc in function_calls:
    if (
        fc.name == REQUEST_CONFIRMATION_FUNCTION_CALL_NAME
        and fc.args
    ):
      original_function_call = fc.args.get("originalFunctionCall", {})
      tool_args = original_function_call.get("args", {})
      if tool_args:
        args_str = "".join(f"\n\t\t{k}: {v}" for k, v in tool_args.items())
      else:
        args_str = " None"
      output.append(f"- Tool name: {original_function_call.get('name', 'N/A')}")
      output.append(
          f"\t- Function call id: {original_function_call.get('id', 'N/A')}"
      )
      output.append(f"\t- Tool args: {args_str}")
  return "\n".join(output)


async def async_input(prompt: str) -> str:
  """Runs synchronous input() in a separate thread."""
  loop = asyncio.get_event_loop()
  return await loop.run_in_executor(None, input, prompt)


def reset_colors_on_interrupt(
    signum: int, frame: Optional[types_module.FrameType]
) -> NoReturn:
  """Resets the terminal colors and raises KeyboardInterrupt."""
  del signum, frame  # Unused.
  print("\x1b[0m")
  raise KeyboardInterrupt()


def sanitized_part(part: types.Part) -> str:
  """Returns a sanitized string representation of expected response parts."""
  if part.thought and part.text:
    return termcolor.colored(
        f"<thought>{part.text}</thought>\n", color="yellow"
    )
  if part.text:
    return part.text
  if part.function_call:
    return f"FunctionCall({part.function_call})"
  if part.function_response:
    response_string = str(part.function_response)
    return (
        f"FunctionResponse({response_string[:256]}"
        f"{'...' if len(response_string) > 256 else ''})"
    )
  if part.executable_code:
    return (
        f"ExecutableCode:\n```{part.executable_code.language}"
        f"\n{part.executable_code.code}\n```")
  if part.code_execution_result:
    result_string = (
        f"outcome={part.code_execution_result.outcome},"
        f" output={part.code_execution_result.output}"
    )
    return (
        f"CodeExecutionResult({result_string[:1024]}"
        f"{'...' if len(result_string) > 1024 else ''})"
    )
  return ""


async def async_run_cli_loop(
    root_agent: Agent,
    session_id: str,
    runner: Runner,
    user_id: str,
    agent_name_to_print_regex: str | None,
):
  """Runs the agent in an asynchronous REPL loop."""
  original_sigint_handler = signal.getsignal(signal.SIGINT)
  signal.signal(signal.SIGINT, reset_colors_on_interrupt)

  readline.parse_and_bind("set editing-mode vi")
  readline.parse_and_bind("set keymap vi-insert")

  clog.green_print(f"Agent: {root_agent.name}")
  clog.green_print(f"Starting {root_agent.name} agent. Type 'exit' to quit.")

  if agent_name_to_print_regex is None:
    agent_name_to_print_regex = ".*"

  pattern = re.compile(agent_name_to_print_regex)
  output_console = Console()
  # A list of tuples of (function_response_id, function_call_id_to_confirm)
  ask_user_confirmation_function_call_ids = []
  try:
    while True:
      user_input = await async_input("\001\x1b[1;32m\002You: \001\x1b[0m\002")
      if user_input.lower() == "exit":
        break

      content = types.Content(role="user", parts=[types.Part(text=user_input)])

      # TODO(b/441586282): Remove the hack once a better solution is in place
      # for cli users to provide function responses.
      if ask_user_confirmation_function_call_ids:
        if not content.parts:
          clog.bold_yellow_print("You haven't entered any text.", end=" ")
          continue

        content.parts = [
            types.Part(
                function_response=types.FunctionResponse(
                    id=id,
                    name='adk_request_confirmation',
                    response={"confirmed": user_input.lower() == "y"},
                )
            )
            for id in ask_user_confirmation_function_call_ids
        ]
        ask_user_confirmation_function_call_ids = []

      with output_console.status("[bold green] Processing..."):
        async for current_event in runner.run_async(
            user_id=user_id, session_id=session_id, new_message=content
        ):
          if current_event.error_message:
            clog.bold_red_print(f"Error: {current_event.error_message}")
          if current_event.content and pattern.fullmatch(current_event.author):
            clog.bold_yellow_print(f"{current_event.author}:", end=" ")
            print(
                f"{''.join(map(sanitized_part, current_event.content.parts))}"
            )

          function_calls_to_ask_user_confirmation = (
              get_ask_user_confirmation_function_calls(
                  current_event
              )
          )
          if function_calls_to_ask_user_confirmation:
            clog.bold_yellow_print(
                "The agent wants to run the following function call(s) which"
                " require user confirmation:"
            )
            clog.bold_yellow_print(
                _format_ask_user_confirmation_requests(
                    function_calls_to_ask_user_confirmation
                )
            )
            clog.bold_yellow_print(
                "\nDo you want to proceed with ALL of them? (y/n)"
            )
            ask_user_confirmation_function_call_ids.extend([
                function_call.id
                for function_call in function_calls_to_ask_user_confirmation
            ])
  finally:
    signal.signal(signal.SIGINT, original_sigint_handler)

  readline.set_completer(None)
  clog.red_print("Exiting agent.")


async def run_repl(
    agent: Agent,
    *,
    runner: Optional[Runner] = None,
    artifact_service: Optional[BaseArtifactService] = None,
    session_service: Optional[BaseSessionService] = None,
    memory_service: Optional[BaseMemoryService] = None,
    agent_name_to_print_regex: Optional[str] = None,
    app_name: Optional[str] = None,
    user_id: str = "test_user_id",
    agents_dir: str = "",
    initial_state: Optional[dict[str, Any]] = None,
    session: Any,
    session_id: Optional[str] = None,
) -> str | None:
  """Runs an agent in a command-line REPL or as a dev server.

  This function will automatically handle the --devserver_mode flag.

  Args:
    agent: The root agent instance to run.
    runner: Runner object.
    artifact_service: The artifact service to use. Defaults to
      InMemoryArtifactService.
    session_service: The session service to use. Defaults to
      InMemorySessionService.
    memory_service: The memory service to use. Defaults to
      InMemoryMemoryService.
    agent_name_to_print_regex: Regex to match which agents' responses to print.
      If None, all are printed.
    app_name: The name of the application. Defaults to the agent's name.
    user_id: The user ID for the session.
    agents_dir: Root directory containing subdirs for agents with those
      containing resources (e.g. .env files, eval sets, etc.) for the agents.
    initial_state: The initial state for the agent.
    session_service: The session service object.


  Returns:
    The session ID if the REPL loop was run, or None if the dev server was
    started.

  """
  app_name = app_name or agent.name
  session_service = (
      session_service or in_memory_session_service.InMemorySessionService()
  )
  memory_service = (
      memory_service or in_memory_memory_service.InMemoryMemoryService()
  )
  artifact_service = (
      artifact_service or in_memory_artifact_service.InMemoryArtifactService()
  )

  runner = runner or Runner(
        app_name=app_name,
        agent=agent,
        artifact_service=artifact_service,
        session_service=session_service,
        memory_service=memory_service)

  current_session = session
  if not current_session:
    current_session = await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        state=initial_state,
        session_id=session_id,
    )

  session_id = session_id or current_session.id

  await async_run_cli_loop(
      root_agent=agent,
      session_id=session_id,
      runner=runner,
      user_id=user_id,
      agent_name_to_print_regex=agent_name_to_print_regex,
  )

  return current_session.id


def get_ask_user_confirmation_function_calls(
    event: event_lib.Event,
) -> list[types.FunctionCall]:
  """Gets the ask user confirmation function calls from the event."""
  if not event.content or not event.content.parts:
    return []
  results = []

  for part in event.content.parts:
    if (
        part
        and part.function_call
        and part.function_call.name
        == 'adk_request_confirmation'
    ):
      results.append(part.function_call)
  return results
