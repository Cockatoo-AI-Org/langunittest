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
