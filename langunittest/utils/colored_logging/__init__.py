"""Colored logging."""
import logging
import termcolor


def blue_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in blue color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='blue'), *args, **kwargs)


def cyan_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in cyan color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='cyan'), *args, **kwargs)


def green_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in green color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='green'), *args, **kwargs)


def grey_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in grey color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='grey'), *args, **kwargs)


def magenta_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in magenta color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='magenta'), *args, **kwargs)


def red_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in red color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='red'), *args, **kwargs)


def yellow_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in yellow color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='yellow'), *args, **kwargs)


# Print (bold).


def bold_blue_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in bold blue color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='blue', attrs=['bold']), *args, **kwargs)


def bold_cyan_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in bold cyan color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='cyan', attrs=['bold']), *args, **kwargs)


def bold_green_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in bold green color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='green', attrs=['bold']), *args, **kwargs)


def bold_grey_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in bold grey color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='grey', attrs=['bold']), *args, **kwargs)


def bold_magenta_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in bold magenta color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(
      termcolor.colored(msg, color='magenta', attrs=['bold']), *args, **kwargs)


def bold_red_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in bold red color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='red', attrs=['bold']), *args, **kwargs)


def bold_yellow_print(msg: str, *args, **kwargs) -> None:
  """Prints `msg` in bold yellow color.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  print(termcolor.colored(msg, color='yellow', attrs=['bold']), *args, **kwargs)


# FATAL.
def fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(msg, *args, **kwargs)


def blue_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in blue color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(termcolor.colored(msg, color='blue'), *args, **kwargs)


def cyan_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in cyan color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(termcolor.colored(msg, color='cyan'), *args, **kwargs)


def green_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in green color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(termcolor.colored(msg, color='green'), *args, **kwargs)


def grey_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in grey color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(termcolor.colored(msg, color='grey'), *args, **kwargs)


def magenta_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in magenta color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(termcolor.colored(msg, color='magenta'), *args, **kwargs)


def red_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in red color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(termcolor.colored(msg, color='red'), *args, **kwargs)


def yellow_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in yellow color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(termcolor.colored(msg, color='yellow'), *args, **kwargs)


# FATAL (bold).


def bold_blue_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold blue color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(
      termcolor.colored(msg, color='blue', attrs=['bold']), *args, **kwargs)


def bold_cyan_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold cyan color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(
      termcolor.colored(msg, color='cyan', attrs=['bold']), *args, **kwargs)


def bold_green_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold green color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(
      termcolor.colored(msg, color='green', attrs=['bold']), *args, **kwargs)


def bold_grey_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold grey color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(
      termcolor.colored(msg, color='grey', attrs=['bold']), *args, **kwargs)


def bold_magenta_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold magenta color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(
      termcolor.colored(msg, color='magenta', attrs=['bold']), *args, **kwargs)


def bold_red_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold red color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(
      termcolor.colored(msg, color='red', attrs=['bold']), *args, **kwargs)


def bold_yellow_fatal(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold yellow color at FATAL severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.fatal(
      termcolor.colored(msg, color='yellow', attrs=['bold']), *args, **kwargs)


# ERROR.
def error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(msg, *args, **kwargs)


def blue_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in blue color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(termcolor.colored(msg, color='blue'), *args, **kwargs)


def cyan_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold cyan color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(termcolor.colored(msg, color='cyan'), *args, **kwargs)


def green_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in green color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(termcolor.colored(msg, color='green'), *args, **kwargs)


def grey_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in grey color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(termcolor.colored(msg, color='grey'), *args, **kwargs)


def magenta_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in magenta color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(termcolor.colored(msg, color='magenta'), *args, **kwargs)


def red_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in red color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(termcolor.colored(msg, color='red'), *args, **kwargs)


def yellow_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in yellow color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(termcolor.colored(msg, color='yellow'), *args, **kwargs)


# ERROR (bold).


def bold_blue_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold blue color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(
      termcolor.colored(msg, color='blue', attrs=['bold']), *args, **kwargs)


def bold_cyan_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold cyan color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(
      termcolor.colored(msg, color='cyan', attrs=['bold']), *args, **kwargs)


def bold_green_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold green color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(
      termcolor.colored(msg, color='green', attrs=['bold']), *args, **kwargs)


def bold_grey_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold grey color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(
      termcolor.colored(msg, color='grey', attrs=['bold']), *args, **kwargs)


def bold_magenta_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold magenta color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(
      termcolor.colored(msg, color='magenta', attrs=['bold']), *args, **kwargs)


def bold_red_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold red color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(
      termcolor.colored(msg, color='red', attrs=['bold']), *args, **kwargs)


def bold_yellow_error(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold yellow color at ERROR severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.error(
      termcolor.colored(msg, color='yellow', attrs=['bold']), *args, **kwargs)


# NOTE: "logging.warn has been deprecated since Python 3.3 and you should use
# logging.warning. Prior to Python 3.3, logging.warn and logging.warning were
# the same function, but logging.warn was not documented, as noted in a closed
# issue in the Python bug tracker http://bugs.python.org/issue13235:"
#
# Source:
# https://stackoverflow.com/questions/15539937/whats-the-difference-between-logging-warn-and-logging-warning-in-python.
#
# Hence *_warn version is NOT provided.

# WARNING.


def warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(msg, *args, **kwargs)


def blue_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in blue color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(termcolor.colored(msg, color='blue'), *args, **kwargs)


def cyan_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in cyan color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(termcolor.colored(msg, color='cyan'), *args, **kwargs)


def green_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in green color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(termcolor.colored(msg, color='green'), *args, **kwargs)


def grey_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in grey color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(termcolor.colored(msg, color='grey'), *args, **kwargs)


def magenta_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in magenta color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(termcolor.colored(msg, color='magenta'), *args, **kwargs)


def red_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in red color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(termcolor.colored(msg, color='red'), *args, **kwargs)


def yellow_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in yellow color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(termcolor.colored(msg, color='yellow'), *args, **kwargs)


# WARNING (bold).


def bold_blue_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold blue color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(
      termcolor.colored(msg, color='blue', attrs=['bold']), *args, **kwargs)


def bold_cyan_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold cyan color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(
      termcolor.colored(msg, color='cyan', attrs=['bold']), *args, **kwargs)


def bold_green_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold green color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(
      termcolor.colored(msg, color='green', attrs=['bold']), *args, **kwargs)


def bold_grey_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold grey color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(
      termcolor.colored(msg, color='grey', attrs=['bold']), *args, **kwargs)


def bold_magenta_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold magenta color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(
      termcolor.colored(msg, color='magenta', attrs=['bold']), *args, **kwargs)


def bold_red_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in red bold color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(
      termcolor.colored(msg, color='red', attrs=['bold']), *args, **kwargs)


def bold_yellow_warning(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold yellow color at WARNING severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.warning(
      termcolor.colored(msg, color='yellow', attrs=['bold']), *args, **kwargs)


# INFO.
def info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(msg, *args, **kwargs)


def blue_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in blue color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(termcolor.colored(msg, color='blue'), *args, **kwargs)


def cyan_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in cyan color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(termcolor.colored(msg, color='cyan'), *args, **kwargs)


def green_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in green color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(termcolor.colored(msg, color='green'), *args, **kwargs)


def grey_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in grey color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(termcolor.colored(msg, color='grey'), *args, **kwargs)


def magenta_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in magenta color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(termcolor.colored(msg, color='magenta'), *args, **kwargs)


def red_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in red color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(termcolor.colored(msg, color='red'), *args, **kwargs)


def yellow_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in yellow color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(termcolor.colored(msg, color='yellow'), *args, **kwargs)


# INFO (bold).


def bold_blue_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold blue color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(
      termcolor.colored(msg, color='blue', attrs=['bold']), *args, **kwargs)


def bold_cyan_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold cyan color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(
      termcolor.colored(msg, color='cyan', attrs=['bold']), *args, **kwargs)


def bold_green_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold green color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(
      termcolor.colored(msg, color='green', attrs=['bold']), *args, **kwargs)


def bold_grey_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold grey color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(
      termcolor.colored(msg, color='grey', attrs=['bold']), *args, **kwargs)


def bold_magenta_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold magenta color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(
      termcolor.colored(msg, color='magenta', attrs=['bold']), *args, **kwargs)


def bold_red_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold red color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(
      termcolor.colored(msg, color='red', attrs=['bold']), *args, **kwargs)


def bold_yellow_info(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold yellow color at INFO severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.info(
      termcolor.colored(msg, color='yellow', attrs=['bold']), *args, **kwargs)


# DEBUG.
def debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(msg, *args, **kwargs)


def blue_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in blue color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(termcolor.colored(msg, color='blue'), *args, **kwargs)


def cyan_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in cyan color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(termcolor.colored(msg, color='cyan'), *args, **kwargs)


def green_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in green color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(termcolor.colored(msg, color='green'), *args, **kwargs)


def grey_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in grey color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(termcolor.colored(msg, color='grey'), *args, **kwargs)


def magenta_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in magenta color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(termcolor.colored(msg, color='magenta'), *args, **kwargs)


def red_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in red color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(termcolor.colored(msg, color='red'), *args, **kwargs)


def yellow_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in yellow color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(termcolor.colored(msg, color='yellow'), *args, **kwargs)


# DEBUG (bold).


def bold_blue_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold blue color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(
      termcolor.colored(msg, color='blue', attrs=['bold']), *args, **kwargs)


def bold_cyan_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold cyan color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(
      termcolor.colored(msg, color='cyan', attrs=['bold']), *args, **kwargs)


def bold_green_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold green color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(
      termcolor.colored(msg, color='green', attrs=['bold']), *args, **kwargs)


def bold_grey_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold grey color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(
      termcolor.colored(msg, color='grey', attrs=['bold']), *args, **kwargs)


def bold_magenta_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold magenta color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(
      termcolor.colored(msg, color='magenta', attrs=['bold']), *args, **kwargs)


def bold_red_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold red color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(
      termcolor.colored(msg, color='red', attrs=['bold']), *args, **kwargs)


def bold_yellow_debug(msg: str, *args, **kwargs) -> None:
  """Logs `msg` in bold yellow color at DEBUG severity.

  Args:
    msg: Log message.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  logging.debug(
      termcolor.colored(msg, color='yellow', attrs=['bold']), *args, **kwargs)
