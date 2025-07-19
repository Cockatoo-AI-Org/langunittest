"""LangUnittest module."""
from __future__ import annotations
from dotenv import load_dotenv, find_dotenv
import os


def load_env(env_path: str | None = None) -> bool:
  """Loads environment variables.

  Args:
    env_path: File path to hold customized environment variables.

  Returns:
    True iff the environment settings is loaded.
  """
  env_path = env_path or '~/.env'
  env_path = os.path.expanduser(env_path)
  if os.path.isfile(env_path):
    return load_dotenv(find_dotenv(env_path))

  return False


load_env()
