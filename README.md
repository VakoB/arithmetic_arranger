# Arithmetic Arranger

This is a Python implementation for arranging arithmetic problems vertically, created as a mini project for FreeCodeCamp.

## Overview

The `arithmetic_arranger` function takes a list of strings representing arithmetic problems and arranges them vertically for better readability. It also has the option to evaluate and display the answers.

## Usage

To use the function, provide a list of arithmetic problems as strings. You can choose to evaluate and display the answers by setting the optional `evaluate` parameter to `True`.

```python
from arithmetic_arranger import arithmetic_arranger

# Example usage:
problems = ["32 + 8", "1 - 3801", "4 - 2", "1000 + 1000", "912 + 3242"]
result = arithmetic_arranger(problems, evaluate=True)
print(result)

# result:

   32         1      4      1000      912
+   8    - 3801    - 2    + 1000    +3242
-----    ------    ----    ------    ------
   40     -3800       2      2000     3154
