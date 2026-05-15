## langunittest: Your Command-line LLM agent for unit test cases.

### Problem
From **[`clippy`](git@github.com:johnklee/langunittest.git)**, you can generate unit test cases for Python modules with ease.

Take the following `math.py` module as an example:

```python
def add(a: float, b: float) -> float:
    return a + b

def div(a: float, b: float) -> float:
    if b == 0.0:
        raise ValueError('Invalid divisor!')
    return a / b
```

You can generate unit test cases using the following command:
```shell
$ pack math.py | clippy 'Create unit test cases for "math.py".'
```

Example AI response:
```python
import unittest
from math import add, div

class TestMathFunctions(unittest.TestCase):

    # Test cases for add()
    def test_add_positive_numbers(self):
        self.assertAlmostEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertAlmostEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertAlmostEqual(add(-1, 2), 1)
        self.assertAlmostEqual(add(1, -2), -1)

    def test_add_with_zero(self):
        self.assertAlmostEqual(add(5, 0), 5)
        self.assertAlmostEqual(add(0, 0), 0)

    def test_add_float_numbers(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

    # Test cases for div()
    def test_div_positive_numbers(self):
        self.assertAlmostEqual(div(6, 2), 3)

    def test_div_negative_numbers(self):
        self.assertAlmostEqual(div(-6, -2), 3)

    def test_div_by_zero(self):
        with self.assertRaisesRegex(ValueError, 'Invalid divisor!'):
            div(10, 0)
        with self.assertRaisesRegex(ValueError, 'Invalid divisor!'):
            div(0, 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```

Current Limitations:
Despite the convenience, this approach comes with several drawbacks:
* ⚠️ The generated test cases are printed to the console and must be copied manually into a file.
* ❌ The test cases may contain errors and are not always executable out of the box.
* 🧠 There’s no memory or iterative refinement; you cannot adjust or fine-tune the generated tests interactively.
* 📉 Test coverage of the generated code is not reported or optimized.

### Introducing langunittest
To address these limitations, we propose `langunittest`, a module designed to provide an interactive agent that works with you to generate, refine, and validate unit tests more efficiently.

Key benefits include:

* 💾 Output saved directly to files—no copy-paste needed.
* ✅ Automatically verified executable test cases.
* 🔄 Interactive back-and-forth refinement with memory and state.
* 📈 Built-in test coverage analysis to ensure sufficient coverage.

With `langunittest`, the goal is to generate reliable, high-quality, and maintainable unit test suites through an iterative and intelligent workflow.

### Usage
Below we will demo how to use `langunittest` to help use create unit test cases.

Firstly, let's use below command to trigger Agent's REPL:
```shell
$ python -m langunittest.agents.agent
...
Starting enterprise_assistant agent. Type 'exit' to quit.
You:
```

Now we can start to interact with agent to write test cases:

1. Setup project root path by entering prompt `Set project root path as /tmp`:
```shell
You: Set project root path as /tmp
...
programming_assistant: Project root path has been set to `/tmp`. How can I help you?
```

**Note**. You can change root path `/tmp` to yours according to real situation.


2. Show the source code of target module:
```shell
You: Show me the source code of utils/my_math.py
...
'''python
def add(a: int, b: int) -> int:
  """Sums up the input `a` and `b`.

  Args:
    a: First value to add
    b: Second value to add

  Returns:
    Return value of `a + b`.
  """
  return a + b
'''
```

3. Ask agent to create tests:
```shell
You: Please create test cases for it.
...
----------------------------------------------------------------------
Ran 4 tests in 0.000s

I've created the following test cases for `utils/my_math.py`:
'''python
import unittest
from utils.my_math import add

class TestMyMath(unittest.TestCase):

    def test_add_positive_numbers(self): # Test adding two positive numbers
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self): # Test adding two negative numbers
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self): # Test adding a positive and a negative number
        self.assertEqual(add(1, -2), -1)

    def test_add_zero(self): # Test adding zero to a number
        self.assertEqual(add(0, 5), 5)

if __name__ == '__main__':
    unittest.main()
'''
```

4. Ask agent to add new test case:
```shell
You: Please add new test case with input 1 and 99.
...
Ran 5 tests in 0.000s

OK
...
'''python
import unittest
from utils.my_math import add

class TestMyMath(unittest.TestCase):
  ...
  def test_add_large_positive_numbers(self): # Test adding 1 and 99
        self.assertEqual(add(1, 99), 100)

if __name__ == '__main__':
    unittest.main()
'''

And here are the results of running all the tests:
'''
--- Custom Test Output ---
test_add_large_positive_numbers (tests.unit.utils.test_my_math.TestMyMath.test_add_large_positive_numbers) ... ok
test_add_mixed_numbers (tests.unit.utils.test_my_math.TestMyMath.test_add_mixed_numbers) ... ok
test_add_negative_numbers (tests.unit.utils.test_my_math.TestMyMath.test_add_negative_numbers) ... ok
test_add_positive_numbers (tests.unit.utils.test_my_math.TestMyMath.test_add_positive_numbers) ... ok
test_add_zero (tests.unit.utils.test_my_math.TestMyMath.test_add_zero) ... ok
==========
Overall Result: OK (All tests passed) ✅
'''
All tests passed successfully!
```

5. Exit the REPL:
```shell
You: exit
Exiting agent.
```
