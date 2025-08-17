"""Module to hold dataclasses, constants uesd for the tools."""
from __future__ import annotations

from collections.abc import Mapping
import dataclasses
from functools import cached_property
import importlib
import langfun as lf
import logging
import os
import pathlib
import pyglove as pg
import sys
from typing import Any
import unittest


Path = pathlib.Path


@dataclasses.dataclass
class ProjectConfig:
  project_root_path: str = sys.argv[0] or os.getcwd()
  reference_files: list[ReferenceFile] = (
      dataclasses.field(default_factory=list))


project_config = ProjectConfig()


# Langfun LLM model.
_LF_MODEL = lf.llms.GeminiPro1_5()


class CustomTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.all_test_results = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.all_test_results.append(f"{test} ... ok")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.all_test_results.append(f"{test} ... FAILED")

    def addError(self, test, err):
        super().addError(test, err)
        self.all_test_results.append(f"{test} ... ERROR")

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.all_test_results.append(f"{test} ... SKIPPED")


class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        # This method tells the runner to use YOUR custom result class
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)


class ReferenceFile(pg.Object):
  """Symbolic class for file served as reference to create the unit test case.

  Attributes:
    file_path: Path of the reference file.
    file_content: Source code of the file.
    is_exist: True if the reference file exist.
  """
  file_path: str

  @property
  def is_exist(self) -> bool:
    return os.path.isfile(self.file_path)

  @cached_property
  def file_content(self) -> str:
    with open(self.file_path) as fo:
      return fo.read()


class TestModule(pg.Object):
    """Symbolic class to hold the target module for generating unit test cases.

    Attributes:
      project_root_path: Path to the project root.
      module_package: Package path of the module.
      module_name: Name of the module.
      module_content: Source code of the module.
      reference_files: Reference files.
    """
    project_root_path: str
    module_package: str
    module_name: str
    module_content: str
    reference_files: list[ReferenceFile]


class UnitTestCases(pg.Object):
    """Symbolic class to hold generated unit test cases.

    Attributes:
      project_root_path: Path to the project root.
      module_package: Package path of the target module.
      module_name: Name of the target module.
        test_case_content: Generated unit test case source code.

      project_root_path: Project root path.
      module_package: Module package path.
      module_name: Module name.
      test_case_content: Content of generated unit test cases.
      test_module_name: Testing module name to hold unit test cases.
      unit_test_root_path: Root path to hold modules of unit test cases.
      unit_test_case_module_dir_path: Directory of testing module to hold unit
        test cases.
      unit_test_case_module_path: Path of testing module to hold the generated
        unit test cases.
      unit_test_case_module_package: Package of unit test case module.
    """
    project_root_path: str
    module_package: str
    module_name: str
    test_case_content: str

    @property
    def test_module_name(self) -> str:
        return f'test_{self.module_name}.py'

    @property
    def unit_test_root_path(self) -> str:
        return str(
            Path(self.project_root_path) / Path('tests/unit'))

    @property
    def unit_test_case_module_dir_path(self) -> str:
        return str(
            Path('tests/unit') / Path(self.module_package.replace('.', '/')))

    @property
    def unit_test_case_module_path(self) -> str:
        return str(
            Path(self.unit_test_root_path) /
            Path(
                self.module_package.replace('.', '/') /
                Path(self.test_module_name)))

    @property
    def unit_test_case_module_package(self) -> str:
        module_name = self.test_module_name.split(".")[0]

        # Find the fully qualified module path
        return (
            f"{self.unit_test_case_module_dir_path}.{module_name}"
        ).replace('/', '.')

    def output(self):
        os.makedirs(
            os.path.dirname(self.unit_test_case_module_path), exist_ok=True)
        with open(self.unit_test_case_module_path, 'w') as fw:
            fw.write(self.test_case_content)


class UnitTestRunner:
    def __init__(self, unit_test_case: UnitTestCases):
        self.unit_test_case = unit_test_case
        self._test_result = None

    def _generate_output(self, result) -> str:
        output_messages = []
        output_messages.append('--- Custom Test Output ---')
        for outcome_string in result.all_test_results:
          output_messages.append(outcome_string)

        output_messages.append('=' * 10)
        if result.wasSuccessful():
          output_messages.append('Overall Result: OK (All tests passed) ✅')
        else:
          output_messages.append('Overall Result: FAILED ❌')

        if result.failures:
          output_messages.append(f'Failures ({len(result.failures)}):')
          for test, traceback_str in result.failures:
            output_messages.append(f'  Test: {test}')
            output_messages.append(f'  Traceback:\n{traceback_str}\n')
        if result.errors:
          output_messages.append(f'Errors ({len(result.errors)}):')
          for test, traceback_str in result.errors:
            output_messages.append(f'  Test: {test}')
            output_messages.append(f'  Traceback:\n{traceback_str}\n')

        if result.skipped:
          output_messages.append(f'Skipped ({len(result.skipped)}):')
          for test, reason in result.skipped:
            output_messages.append(f'  Test: {test}, Reason: {reason}\n')
        if result.expectedFailures:
          output_messages.append(
              f'Expected Failures ({len(result.expectedFailures)}):')
          for test, traceback_str in result.expectedFailures:
            output_messages.append(f'  Test: {test}')
            output_messages.append(f'  Traceback:\n{traceback_str}\n')
        if result.unexpectedSuccesses:
          output_messages.append(
              f'Unexpected Successes ({len(result.unexpectedSuccesses)}):')
          for test in result.unexpectedSuccesses:
            output_messages.append(f'  Test: {test}\n')

        return '\n'.join(output_messages)

    def run(self) -> str:
        project_root = self.unit_test_case.project_root_path
        if project_root not in sys.path:
          sys.path.insert(0, project_root)

        # Output unit test cases into testing module.
        self.unit_test_case.output()

        # Remove from sys.modules if already loaded
        fq_module_name = self.unit_test_case.unit_test_case_module_package
        logging.debug('Removing module "%s"', fq_module_name)
        if fq_module_name in sys.modules:
          del sys.modules[fq_module_name]

        test_module = importlib.import_module(fq_module_name)
        importlib.reload(test_module)

        # Optionally clear all test modules from cache
        for name in list(sys.modules.keys()):
          if name.startswith(
              self.unit_test_case.module_package) and "test_" in name:
            del sys.modules[name]

        # Discover tests from the 'tests' directory
        # start_dir: The directory to start searching for tests (e.g., 'tests')
        # pattern: Only look for files matching this pattern (e.g., 'test_*.py')
        test_loader = unittest.TestLoader()
        logging.info(
            'Start dir: %s',
            self.unit_test_case.unit_test_case_module_dir_path)
        logging.info(
            'Test module name: %s',
            self.unit_test_case.test_module_name.split(".")[0])

        test_suite = test_loader.loadTestsFromModule(test_module)
        # Run the tests
        runner = CustomTestRunner(verbosity=0)  # verbosity=2 shows more details
        self._test_result = runner.run(test_suite)
        return self._generate_output(self._test_result)


def _read_module_content(
    project_root_path: str,
    module_package: str,
    module_name: str) -> str:
  module_path = str(
      Path(project_root_path) /
      Path(module_package.replace('.', '/')) /
      Path(f'{module_name}.py'))
  if not os.path.isfile(module_path):
    raise ValueError(f'Module path "{module_path}" does not exist!')

  module_content = open(module_path, 'r').read()
  return module_content


def add_reference_file(file_path: str):
  """Adds reference files for further process in creating test cases.

  Args:
    file_path: File path of reference file to be added.

  Returns:
    A dictionary containing the result of executing this function.
    The key definition of the returned dictionary:
    - `status`: `True` if the given reference file is added successfully.
    - `result`: The absolute path of the added reference file.
    - `error`: Error message for `status` as False.
  """
  if not file_path.startswith('/'):
    # Relative path. Join it with project root path.
    file_path = str(
        Path(project_config.project_root_path) / Path(file_path))

  reference_file = ReferenceFile(file_path=file_path)
  if not reference_file.is_exist:
    return {
        'status': False,
        'result': '',
        'error': f'Given file path "{file_path}" does not exist!',
    }

  project_config.reference_files.append(reference_file)
  return {
      'status': True,
      'result': file_path,
      'error': '',
  }


def read_module_content(
    module_package: str,
    module_name: str) -> Mapping[str, Any]:
  """Reads and loads the content of module which will be tested.

  Args:
    module_package: Package path of the module.
    module_name: Name of the module.

  Returns:
    A dictionary containing the result of executing this function.
    The key definition of the returned dictionary:
    - `status`: `True` if the test case content is loaded successfully.
    - `module_content`: The loaded content of module.
    - `error`: Error message collected in the process.
  """
  try:
    module_content = _read_module_content(
        project_root_path=project_config.project_root_path,
        module_package=module_package,
        module_name=module_name)
    return {
        'status': True,
        'module_content': module_content,
        'error': '',
    }
  except Exception as ex:
    logging.warning(
        'Failed to read module content! Error: %s',
        ex, exc_info=True)
    return {
        'status': False,
        'module_content': '',
        'error': str(ex),
    }


def read_exist_test_cases(
    module_package: str,
    module_name: str) -> Mapping[str, Any]:
  """Reads and loads the exist test cases content if exist.

  Args:
    module_package: Package path of the module.
    module_name: Name of the module.

  Returns:
    A dictionary containing the result of executing this function.
    The key definition of the returned dictionary:
    - `status`: `True` if the test case content is loaded successfully.
    - `test_module_path`: The path of generated testing module to hold test
      cases.
    - `test_case_content`: The test case content of given module information.
    - `error`: Error message collected in the process.
  """
  unit_test_case_info = UnitTestCases(
      project_root_path=project_config.project_root_path,
      module_name=module_name,
      module_package=module_package,
      test_case_content='')
  if not os.path.isfile(unit_test_case_info.unit_test_case_module_path):
    return {
        'status': False,
        'test_module_path': unit_test_case_info.unit_test_case_module_path,
        'test_case_content': '',
        'error': (
            f'The file "{unit_test_case_info.unit_test_case_module_path}" '
            'of expected module to hold test cases does not exist.'),
    }

  test_case_content = open(
      unit_test_case_info.unit_test_case_module_path, 'r').read()
  return {
      'status': True,
      'test_module_path': unit_test_case_info.unit_test_case_module_path,
      'test_case_content': test_case_content,
      'error': '',
  }


def write_test_cases(
    module_package: str,
    module_name: str,
    test_case_content: str) -> Mapping[str, Any]:
  """Writes or output the generated test case content into file system.

  Args:
    module_package: Package path of the module.
    module_name: Name of the module.
    test_case_content: Generated test Case content.

  Returns:
    A dictionary containing the result of executing this function.
    The key definition of the returned dictionary:
    - `status`: `True` if the test case content is output successfully.
    - `test_module_path`: The path of generated testing module to hold test
      cases.
    - `error`: Error message collected in the process.
  """
  unit_test_case_info = UnitTestCases(
      project_root_path=project_config.project_root_path,
      module_name=module_name,
      module_package=module_package,
      test_case_content=test_case_content)

  unit_test_case_info.output()
  return {
      'status': True,
      'test_module_path': unit_test_case_info.unit_test_case_module_path,
      'error': '',
  }


def create_test_cases(
    module_package: str,
    module_name: str,
    additional_request: str = '') -> Mapping[str, Any]:
  """Creates unit test cases for given module `test_module`.

  Args:
    module_package: Package path of the module.
    module_name: Name of the module.
    additional_request: Additional request to create test cases.

  Returns:
    A dictionary containing the result of executing this function.
    The key definition of the returned dictionary:
    - `status`: `True` if the created test case(s) can all pass.
    - `outpupt`: The execution output of the created test case(s).
    - `test_module_path`: The path of generated testing module to hold test
      cases.
    - `test_module_content`: The content of generated test cases.
    - `error`: Error message collected in the process.
  """
  try:
    module_content = _read_module_content(
        project_root_path=project_config.project_root_path,
        module_package=module_package,
        module_name=module_name)
  except Exception as ex:
    logging.warning(
        'Failed to read module content! Error: %s',
        ex, exc_info=True)
    return {
        'status': False,
        'output': '',
        'test_module_path': '',
        'error': str(ex),
    }

  logging.debug('@module_package: %s', module_package)
  logging.debug('@module_name:%s', module_name)
  logging.debug(
      '@project_root_path: %s',
      project_config.project_root_path)
  test_module = TestModule(
      project_root_path=project_config.project_root_path,
      module_name=module_name,
      module_package=module_package,
      module_content=module_content,
      reference_files=project_config.reference_files)

  tmp_unit_test_case = UnitTestCases(
      project_root_path=project_config.project_root_path,
      module_name=module_name,
      module_package=module_package,
      test_case_content='')

  exist_test_module_path = tmp_unit_test_case.unit_test_case_module_path
  if os.path.isfile(exist_test_module_path):
    test_module.reference_files.append(
        ReferenceFile(file_path=exist_test_module_path))

  prompt = (
      'Please create unit test cases for {{module}}'
      if not additional_request else
      'Please improve the unit test cases of {{module}} by request: ' +
      f'{additional_request}')

  if os.path.isfile(exist_test_module_path):
    prompt += (
        '; and incrementally leverage exist testing module '
        f'"{exist_test_module_path}"'
        " to maintain unit test cases.")

  logging.debug('Prompt: %s', prompt)
  unit_test_case_result = lf.query(
      prompt=prompt,          # Prompt to request the generation of test cases.
      schema=UnitTestCases,   # Type annotation as the schema of output object.
      lm=_LF_MODEL,           # The language model to use.
      module=test_module,     # The value of placeholder '{{module}}'
  )

  test_runner = UnitTestRunner(unit_test_case_result)
  testing_result = test_runner.run()
  is_success = 'Overall Result: OK' in testing_result
  return {
      'status': is_success,
      'output': testing_result,
      'test_module_path': unit_test_case_result.unit_test_case_module_path,
      'test_module_content': unit_test_case_result.test_case_content,
      'error': '',
  }


def get_project_root_path() -> dict[str, Any]:
  """Gets project root path.

  Returns:
    A dictionary containing the result of executing this function.
    The key definition of the returned dictionary:
    - `status`: `True` if done.
    - `result`: The obtained project root path.
  """
  return {
      'status': True,
      'result': project_config.project_root_path}


def run_test_cases(
    module_package: str,
    module_name: str,) -> Mapping[str, Any]:
  """Runs test cases of give module.

  Args:
    module_package: Package path of the module.
    module_name: Name of the module.

  Returns:
    A dictionary containing the result of executing this function.
    The key definition of the returned dictionary:
    - `status`: `True` if the created test case(s) can all pass.
    - `outpupt`: The execution output of the created test case(s).
    - `test_module_path`: The path of testing module to hold test cases.
    - `test_module_content`: The content of test cases.
    - `error`: Error message collected in the process.
  """
  unit_test_case_info = UnitTestCases(
      project_root_path=project_config.project_root_path,
      module_name=module_name,
      module_package=module_package,
      test_case_content='')

  test_module_path = unit_test_case_info.unit_test_case_module_path
  if not os.path.isfile(test_module_path):
    return {
        'status': False,
        'output': '',
        'test_module_path': test_module_path,
        'test_module_content': '',
        'error': f'Test module {test_module_path} does not exist!',
    }

  unit_test_case_info = UnitTestCases(
      project_root_path=project_config.project_root_path,
      module_name=module_name,
      module_package=module_package,
      test_case_content=open(test_module_path, 'r').read())

  test_runner = UnitTestRunner(unit_test_case_info)
  testing_result = test_runner.run()
  is_success = 'Overall Result: OK' in testing_result
  return {
      'status': is_success,
      'output': testing_result,
      'test_module_path': test_module_path,
      'test_module_content': unit_test_case_info.test_case_content,
      'error': '',
  }


def set_project_root_path(project_root_path: str) -> dict[str, Any]:
  """Sets or changes the project root path.

  Args:
    project_root_path: The project root path of module(s) which we will create
      test cases for.

  Returns:
    A dictionary containing the result of executing this function.
    The key definition of the returned dictionary:
    - `status`: `True` if done.
    - `error`: The error message.
  """
  if not project_root_path.startswith('/'):
    project_root_path = str(Path(sys.argv[0]) / Path(project_root_path))

  if not os.path.isdir(project_root_path):
    return {
        'status': False,
        'error': (
            f'Given project root path "{project_root_path}" does not exist!'),
    }

  project_config.project_root_path = project_root_path
  return {
      'status': True,
      'error': '',
  }
