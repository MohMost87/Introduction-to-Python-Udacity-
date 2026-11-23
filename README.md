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



### Importance of Comments in Python Coding

Comments are vital in Python programming for clearer understanding and collaboration among developers. They provide insight into why code behaves a certain way or what a section does, making a repository easier to read and maintain.

#### Why Use Comments?
- **Human Readability:** Comments provide clear, human-readable context alongside code.
- **Ignored at Runtime:** Python ignores `#` comments during execution, so they have zero impact on runtime behavior or performance.
- **Clarity:** Helpful for explaining non-obvious logic, edge cases, conditions, and workflows.

#### How to Add Comments & Docstrings
- **Single-line & Block Comments (`#`):** Prefix lines with `#` for single-line notes or consecutive `#` lines for block comments. *(Note: Triple quotes `"""..."""` or `'''...'''` create multi-line string literals—used as **docstrings** when placed right after a `def`, `class`, or module—rather than true comments.)*
- **Docstrings (`"""..."""`):** Placed immediately below a `def` or `class` header to document purpose, parameters/arguments, and return values.

#### Best Practices & Example
- Explain **why** a condition or branch exists (such as `if` / `else` logic) rather than repeating what the code already says.
- Use docstrings right after function definitions to document arguments and return values.

```python
def calculate_discount(price, is_member):
    """Calculate the final price after applying a member discount.

    Args:
        price (float): Original item price.
        is_member (bool): Whether the buyer has an active membership.

    Returns:
        float: Final price after any applicable discount.
    """
    # Apply a 15% discount only for active members on positive prices
    if is_member and price > 0:
        return price * 0.85

    # Non-members pay the standard price
    return price
```
### Python Basics: Data Types & Control Flow

Learn the foundational elements of Python programming through essential data types, Boolean control flow, and supporting numeric/text representations.

#### Python Data Types
- **Literals:** Fixed values written directly into source code (such as numbers, strings, booleans, or `None`).
- **Booleans:** `True` or `False` values (`bool`) used for conditions, comparisons, and decision-making.
- **Integers and Floats:** Numeric types where `int` represents whole numbers without a decimal point (`-3`, `0`, `42`) and `float` represents floating-point numbers with a decimal point (`3.14`, `-0.5`, `2.0`).

```python
# Literals & basic data types
is_active = True       # bool literal
retries = 3            # int literal
threshold = 0.75       # float literal
status_label = "Ready" # str literal
```

#### While Loops and Booleans
- **Purpose:** A `while` loop repeats a block of code as long as a condition evaluates to `True`, stopping once the Boolean state becomes `False`.
- **Example:** Simulating a browser plugin that stays active while the user is engaged and enters sleep mode to conserve resources once engagement stops.

```python
user_engaged = True
idle_cycles = 0

while user_engaged:
    print("Plugin active: monitoring current tab...")
    idle_cycles += 1

    # Simulate user going idle after 3 checks
    if idle_cycles >= 3:
        user_engaged = False

print("Plugin sleeping to conserve resources.")
```

#### Additional Concepts
- **Strings:** Ordered sequences of characters (`str`) enclosed in single (`'...'`), double (`"..."`), or triple quotes, commonly used for messages, labels, or titles.
- **Scientific Notation:** Compact way to write very large or very small `float` values using `e` or `E` (representing powers of 10).
- **Binary Systems:** Base-2 numeral systems (`0` and `1`) fundamental to computing; Python lets you write binary literals with a `0b` prefix and convert integers with `bin()`.

```python
# Strings
welcome_msg = 'Welcome to the workspace'
report_title = "Q4 Latency Summary"

# Scientific notation (floats)
planck_like_scale = 1.5e-4  # 0.00015
large_sample_size = 2.5e6   # 2500000.0

# Binary systems
permissions_mask = 0b101    # Decimal 5 (binary 101)
print(bin(permissions_mask))  # '0b101'
```
### Understanding Numbers and Strings in Python

Python supports several numeric types, number-base prefixes, and text sequences (`str`) out of the box.

#### Exploring Different Types of Numbers
- **Integers (`int`):** Positive or negative whole numbers without a decimal point—useful for counts (apples, cars) or whole time units.
- **Floating Point Numbers (`float`):** Numbers with a decimal point for fractional or non-whole values such as prices (`4.99`) or measurements.
- **Scientific Notation:** Shorthand using `e` or `E` (powers of 10) to write very large or very small `float` values cleanly, such as `1e6` for `1000000.0`.

```python
# Integers
apples = 12
cars = -2
elapsed_seconds = 90

# Floating point numbers
item_price = 4.99
tax_rate = 0.15

# Scientific notation (produces float values)
million = 1e6          # 1000000.0
micro_step = 2.5e-4    # 0.00025
```

#### Numbers with Various Bases
Python integer literals can be written in different numeral bases using prefixes, all evaluating to standard integer values in Python:
- **Binary (Base 2):** Digits `0`–`1` with a `0b` prefix (e.g., `0b1010` equals `10`).
- **Octal (Base 8):** Digits `0`–`7` with a `0o` prefix (e.g., `0o12` equals `10`).
- **Decimal (Base 10):** Standard base-10 digits `0`–`9` with no prefix (e.g., `10`).
- **Hexadecimal (Base 16):** Digits `0`–`9` and letters `A`–`F` (case-insensitive) with a `0x` prefix (e.g., `0xA` equals `10`).

```python
binary_num = 0b1010    # 10
octal_num = 0o12       # 10
decimal_num = 10       # 10
hex_num = 0xA          # 10

print(binary_num, octal_num, decimal_num, hex_num)  # 10 10 10 10
print(bin(10), oct(10), hex(10))                    # '0b1010' '0o12' '0xa'
```

#### Introduction to Strings
- **Strings (`str`):** Text sequences enclosed in single (`'...'`) or double (`"..."`) quotes (and triple quotes for multi-line text), assigned to variables for messages, labels, or status text such as `"Login successful."`.

```python
status_message = "Login successful."
username = 'alex_dev'
greeting = f"Welcome back, {username}! {status_message}"

print(greeting)  # Welcome back, alex_dev! Login successful.
```
### Understanding Python Variables

Python variables store and manage data so you can reference, reuse, and update values across your code without retyping literals every time.

#### Definition
- **Named References / Containers:** Variables bind a name to a value in memory so you can recall or update it later.
- **Assignment Syntax:** Created using the `=` assignment operator (for example, `x = 100`).

#### Properties
- **Dynamic Lifecycle:** Variables can be assigned, reassigned/updated, deleted with `del`, and recreated later in a program.
- **Dynamic Typing:** A variable name can point to values of different types over time as program state changes.

#### Naming Conventions
- **Use `snake_case`:** Separate lowercase words with underscores (such as `user_name` or `total_score`), following PEP 8.
- **Valid Characters Only:** Start with a letter or underscore (`_`), use letters, digits, and underscores only, and avoid spaces, hyphens, special symbols, or reserved Python keywords.

#### Examples of Use: Division with Error Handling
Using variables inside a function with `try` / `except` shows how values can be validated, computed, and safely returned when edge cases like division by zero occur.

```python
def safe_divide(dividend, divisor):
    """Divide two numbers safely, returning None if division by zero occurs."""
    try:
        quotient = dividend / divisor
        return quotient
    except ZeroDivisionError:
        error_message = "Cannot divide by zero."
        print(error_message)
        return None


# Creating and updating variables
first_number = 24
second_number = 6
result = safe_divide(first_number, second_number)  # 4.0

# Reassigning and testing division by zero
second_number = 0
fallback_result = safe_divide(first_number, second_number)  # Prints error, returns None

# Deleting a variable when no longer needed
del fallback_result
```
