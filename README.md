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

Firstly, let's use below command to launch Python REPL:
```shell
$ python -m asyncio
>>>
```

Then we enter below line to launch agent to write test cases:
```python
# Import langunittest:
>>> from langunittest.agents import agent

# Instantiated an agent:
>>> tc_agent = await agent.TCAgent.create()

# Start to interact with agent:
>>> await tc_agent.interact_async()
```

Not It is ready interact with agent to write test cases:

1. Setup project root path:
```
[User] $ Set project root path as /tmp
...
[Agent] # OK. The project root path has been set to /tmp.
```

2. Show the source code of target module:
```
[User] $ Show me the source code of utils/my_math.py
...
[Agent] # The source code is as:
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
```
[User] $ Please create test cases for it.
...
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
[Agent] # Great! All test cases passed. Here is the test code I generated:

'''python
import unittest
from utils.my_math import add

class TestMyMath(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)

    def test_add_zero(self):
        self.assertEqual(add(2, 0), 2)

if __name__ == '__main__':
    unittest.main()
'''
```

4. Ask agent to modify tests:
```
[User] $ Pleaes add one line comment to each test cases.
...
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
[Agent] # Excellent, all tests passed! Here's the updated test code with comments:

'''python
import unittest
from utils.my_math import add

class TestMyMath(unittest.TestCase):

    def test_add_positive_numbers(self):
        # Test adding two positive numbers
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        # Test adding two negative numbers
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        # Test adding a positive and a negative number
        self.assertEqual(add(2, -3), -1)

    def test_add_zero(self):
        # Test adding a number with zero
        self.assertEqual(add(2, 0), 2)

if __name__ == '__main__':
    unittest.main()
'''
```
