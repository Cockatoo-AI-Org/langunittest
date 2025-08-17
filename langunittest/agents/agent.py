"""Langunittest agent to facilitate writting unit test cases."""
from __future__ import annotations

import logging
import asyncio  # noqa: F401

from google.adk.agents import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService  # noqa: E501
from google.adk.tools.base_toolset import BaseTool
from google.adk.sessions import Session
from google.genai import types

from langunittest.agents import tools as test_case_tools


_AGENT_INSTRUCTIONS = """
**Persona:** You are a senior Python programmer specializing in software testing
. Your expertise is in crafting comprehensive, readable, and effective unit
tests.

**Primary Goal:** Your mission is to assist users in generating high-quality
unit test cases for their Python modules. You will prioritize creating readable
tests and will actively use test results to fix any failures in the generated
code.

---

**Working Flow**

1.  **Project Context:**
    * The user will provide a relative path to the project's root directory.
    * To change the project root, the user will explicitly ask you, and you will
    respond by calling `set_project_root_path`.

2.  **Module Identification:**
    * Users will specify the target module for testing in one of two ways:
        * **As a package name:** e.g., `utils.my_math`. From this, you must
          extract the **module package** (`utils`) and
          **module name** (`my_math`).
        * **As a file path:** e.g., `utils/my_math.py`. From this, you must
          extract the **module package** (`utils`) and
          **module name** (`my_math`).

3.  **Core Actions:**
    * **Load Module:** Before writing tests, you must call `read_module_content`
      to load the module's code. Another situation you need to load module is that
      the users ask you to show them the source code of the module.
    * **Load Existing Tests:** Always call `read_exist_test_cases` to load and
      incrementally update existing tests. Ignore this step if no test exist.
    * **Write Tests:** After generating the tests, call `write_test_cases` to
      output them.
    * **Run Tests:** You can run tests in two scenarios:
        * When a user explicitly asks you to.
        * Immediately after you call `write_test_cases` to validate your
          generated code.
    * **Debugging:** If the `run_test_cases` tool reports any failures, use the
      output to debug and correct the generated test cases before trying again.
      Always display the test output to the user, regardless of whether it
      passes or fails.
"""

_AGENT_MODEL = 'gemini-2.0-flash'
_TOOLS = (
    test_case_tools.read_exist_test_cases,
    test_case_tools.read_module_content,
    test_case_tools.write_test_cases,
    test_case_tools.get_project_root_path,
    test_case_tools.set_project_root_path,
    test_case_tools.run_test_cases,
)


class TCAgent:
  model_name: str
  agent_name: str
  root_agent: LlmAgent
  runner: Runner
  session: Session
  llm_last_query_resp: str

  @classmethod
  async def create(
      cls,
      app_name: str = 'test_case_creator_app',
      model_name: str = _AGENT_MODEL,
      agent_name: str = 'enterprise_assistant',
      instruction: str = _AGENT_INSTRUCTIONS,
      tools: list[BaseTool] | None = None,
      user_id: str = 'user_tc') -> TCAgent:
    self = TCAgent()
    self.model_name = model_name
    self.agent_name = agent_name
    tools = tools or list(_TOOLS)
    self.root_agent = LlmAgent(
        model=model_name,
        name=agent_name,
        instruction=instruction,
        tools=tools,
    )
    session_service = InMemorySessionService()
    # Artifact service might not be needed for this example
    artifacts_service = InMemoryArtifactService()
    self.session = await session_service.create_session(
        state={}, app_name=app_name, user_id=user_id)

    self.runner = Runner(
        app_name=app_name,
        agent=self.root_agent,
        artifact_service=artifacts_service,
        session_service=session_service)

    return self

  async def query_async(self, query_str: str) -> str:
    logging.debug("User Query: '%s'", query_str)
    content = types.Content(
        role='user',
        parts=[types.Part(text=query_str)])

    logging.debug("Running agent...")
    events_async = self.runner.run_async(
        session_id=self.session.id,
        user_id=self.session.user_id,
        new_message=content)

    async for event in events_async:
      if event.is_final_response():
        final_response = event.content.parts[0].text
        self.llm_last_query_resp = final_response
        return final_response

    return '?'

  async def interact_async(self, exit_signals={'bye', 'exit', 'quit', 'q'}):
    while True:
      user_query = input('[User] $ ')
      if user_query.strip() in exit_signals:
        print('[Agent] # Bye!')
        break

      resp = await self.query_async(user_query)
      print(f'[Agent] # {resp}')


root_agent = Agent(
    model=_AGENT_MODEL,
    name='root_agent',
    description=(
        'Receive instructions from user and create test cases on the provided '
        'module information'),
    instruction=_AGENT_INSTRUCTIONS,
    tools=list(_TOOLS))
