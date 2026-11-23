# Introduction-to-Python-Udacity

# Understanding Python Keywords and Structure
Learning Python involves understanding its lexis and keywords, which serve as building blocks for creating functions and scripts. These reserved words carry special meanings within the Python language:

### Python Core Keywords

`if`: Used for conditional statements.<br>
`else`: Specifies what to do if the `if` condition is false.<br>
`elif`: Short for "else if," allows multiple conditions.<br>
`for`: Initiates loops to iterate over a sequence or iterable.<br>
`while`: Creates a loop where actions continue while a condition is true.<br>
`def`: Defines a new function.<br>
`return`: Returns a value from a function.<br>

### Truthiness Check (`if` / `else`)

```python
if my_variable:
    print("Hello world.")
else:
    print("World, Hello.")


### Understanding Python Indentation Errors

Indentation is critical in Python because it defines code blocks, nesting, and execution flow rather than braces (`{}`) or keywords. Improper alignment raises `IndentationError` and prevents the script from running.

#### Example Function (`greet_function`)
- Prints `Hello, {name}` when a truthy/non-empty `name` is provided.
- Prints `Hello, World` when `name` is empty or `None`.

```python
def greet_function(name):
    if name:
        print(f"Hello, {name}")
    else:
        print("Hello, World")
```

#### Common Indentation Mistakes
- **Importance of Indentation:** Proper alignment is required to execute Python scripts. Mixing tabs and spaces inconsistently or misaligning lines triggers `IndentationError`.
- **Misplacing the `else` clause:** `else` must align at the exact same indentation level as its matching `if`. Misaligning it causes syntax/indentation errors (such as expecting an indented block or mismatched block level).
- **Misaligning function contents:** Statements inside `def` must share uniform indentation (PEP 8 recommends **4 spaces** per level). Extra or uneven indentation disrupts block structure and causes errors.

#### Resolving Indentation Issues
- Realigning lines to a consistent indent level (typically **4 spaces** per block) resolves `IndentationError` so the script executes cleanly.


### Python Keywords Cheat Sheet

| Keyword | Explanation | Example |
| :--- | :--- | :--- |
| `False` | Represents a Boolean false value | `x = False` |
| `True` | Represents a Boolean true value | `x = True` |
| `None` | Represents the absence of a value or null | `x = None` |
| `and` | Logical AND operator. Returns `True` if both conditions are true | `if x > 0 and y > 0:` |
| `or` | Logical OR operator. Returns `True` if at least one condition is true | `if x > 0 or y > 0:` |
| `not` | Logical NOT operator. Reverses the truth value | `if not x:` |
| `as` | Used for aliasing (e.g., modules or exceptions) | `import numpy as np` |
| `assert` | Used for debugging; checks if a condition is true | `assert x > 0, "x must be positive"` |
| `break` | Exits a loop prematurely | `for i in range(5): break` |
| `class` | Defines a class | `class MyClass:` |
| `continue` | Skips the rest of the loop iteration | `for i in range(5): continue` |
| `def` | Defines a function | `def my_function():` |
| `del` | Deletes an object or variable | `del x` |
| `elif` | Else-if condition in an `if` statement | `if x > 0: ... elif x == 0:` |
| `else` | Defines the block of code executed if all conditions fail | `if x > 0: ... else:` |
| `except` | Handles exceptions in a `try` block | `try: pass except Exception:` |
| `finally` | Defines cleanup actions after `try`-`except` blocks | `try: pass finally: cleanup()` |
| `for` | Starts a `for` loop | `for i in range(5):` |
| `from` | Imports specific parts of a module | `from math import pi` |
| `global` | Declares a global variable | `global x; x = 5` |
| `if` | Starts a conditional block | `if x > 0:` |
| `import` | Imports a module | `import os` |
| `in` | Checks membership or iteration | `if x in items:` |
| `is` | Tests object identity | `if x is y:` |
| `lambda` | Defines an anonymous function | `lambda x: x * 2` |
| `nonlocal` | Refers to a variable in the nearest enclosing scope | `nonlocal x` |
| `pass` | Does nothing; a placeholder | `pass` |
| `raise` | Triggers an exception | `raise ValueError("Error!")` |
| `return` | Returns a value from a function | `return x` |
| `try` | Starts a block of code to handle exceptions | `try: pass` |
| `while` | Starts a `while` loop | `while x > 0:` |
| `with` | Simplifies resource management (e.g., file handling) | `with open('file.txt') as f:` |
| `yield` | Pauses and returns a value from a generator | `yield x` |

