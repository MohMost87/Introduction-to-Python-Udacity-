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
### Understanding Python Operators

Operators are special symbols or keywords in Python that perform operations on values and variables (operands), such as math calculations, comparisons, logic checks, and assignments.

#### Arithmetic Operators
Used for mathematical calculations on numeric values:
- `+` (Addition), `-` (Subtraction), `*` (Multiplication), `/` (True division returning a `float`)
- `//` (Floor division rounding down toward negative infinity), `%` (Modulo / remainder), `**` (Exponentiation / power)

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333333333333335
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

#### Assignment & Compound Assignment Operators
Used to assign values to variables and update them in place:
- `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

```python
score = 50
score += 25   # score becomes 75
score //= 3   # score becomes 25
score **= 2   # score becomes 625
```

#### Comparison Operators
Compare two values and return a Boolean (`True` or `False`):
- `==` (Equal to), `!=` (Not equal to), `>` (Greater than), `<` (Less than), `>=` (Greater than or equal to), `<=` (Less than or equal to)

```python
x = 10
y = 20

print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x >= 10) # True
```

#### Logical, Membership, and Identity Operators
- **Logical (`and`, `or`, `not`):** Combine or invert Boolean conditions (with short-circuit evaluation).
- **Membership (`in`, `not in`):** Check whether a value exists inside a sequence or collection (such as a list, string, or tuple).
- **Identity (`is`, `is not`):** Check whether two references point to the exact same object in memory (commonly used with `None`).

```python
is_logged_in = True
has_access = False

# Logical
print(is_logged_in and not has_access)  # True
print(is_logged_in or has_access)       # True

# Membership
allowed_roles = ["admin", "editor"]
print("admin" in allowed_roles)         # True

# Identity
token = None
print(token is None)                    # True
```

### Mastering Python Operators

Gain familiarity with core Python arithmetic operators used for mathematical and numerical calculations, ordered below roughly from higher to lower precedence (`**` before `*`, `/`, `//`, `%` before `+`, `-`).

#### Arithmetic Operators Overview
- **Exponentiation (`**`):** Raises a base number to the power of an exponent (e.g., `10 ** 3` produces `1000`).
- **Multiplication (`*`):** Multiplies two numbers (e.g., `10 * 3` equals `30`).
- **Division (`/`):** Divides one number by another and always returns a `float` (e.g., `10 / 3` evaluates to `3.3333333333333335`).
- **Modulus (`%`):** Returns the remainder after dividing one number by another (e.g., `10 % 3` returns `1` because `3 * 3 = 9` with `1` remaining).
- **Floor Division (`//`):** Divides one number by another and floors the quotient down to an integer/whole value (e.g., `10 // 3` equals `3`).
- **Addition (`+`):** Adds two numbers together (e.g., `10 + 3` equals `13`).
- **Subtraction (`-`):** Subtracts the right operand from the left operand (e.g., `10 - 3` equals `7`).

```python
a = 10
b = 3

print(a ** b)  # 1000  (Exponentiation)
print(a * b)   # 30    (Multiplication)
print(a / b)   # 3.3333333333333335 (Division -> float)
print(a % b)   # 1     (Modulus -> remainder)
print(a // b)  # 3     (Floor division -> floored quotient)
print(a + b)   # 13    (Addition)
print(a - b)   # 7     (Subtraction)
```

#### Practical Example: Converting Total Seconds & Checking Even/Odd
Combining floor division (`//`), modulo (`%`), and multiplication/addition shows how arithmetic operators work together in real scripts.

```python
total_seconds = 195
minutes = total_seconds // 60      # 3 full minutes
remaining_seconds = total_seconds % 60  # 15 leftover seconds

print(f"{total_seconds}s = {minutes}m {remaining_seconds}s")  # 195s = 3m 15s

# Using modulo (%) to check if a number is even or odd
number = 10
is_even = (number % 2) == 0
print(f"Is {number} even? {is_even}")  # Is 10 even? True

# Using exponentiation (**) to calculate compound growth (e.g., 100 * 1.05^2)
principal = 100
growth_factor = 1.05 ** 2
print(round(principal * growth_factor, 2))  # 110.25
```
### Floor Division (`//`) in Python

Floor division (`//`) divides two numbers and rounds the result **down** toward negative infinity (the largest integer less than or equal to the exact quotient).

#### How Floor Division Works
- **Returns an `int` or `float`:** If both operands are integers (`int`), the result is an `int`. If either operand is a `float` (or uses scientific notation), the result is a `float` (e.g., `3.0`).
- **Rounds Down, Not Toward Zero:** For positive numbers, `//` looks like truncating decimals, but for negative numbers it rounds further negative (toward $-\infty$).
- **Common Use Cases:** Breaking quantities into full groups/pages, converting time units (seconds to minutes/hours), and pairing with modulo (`%`) to get quotient and remainder together.

```python
# Positive numbers: rounds down to whole units
print(10 // 3)     # 3     (10 / 3 = 3.333... -> 3)
print(19 // 5)     # 3     (19 / 5 = 3.8      -> 3)

# Float operands: returns a float value
print(10.0 // 3)   # 3.0
print(10 // 3.0)   # 3.0

# Negative numbers: rounds toward negative infinity (-3.333... -> -4)
print(-10 // 3)    # -4
print(10 // -3)    # -4
```

#### Practical Examples: Pagination & Time Breakdown
Floor division is especially handy for calculating page counts or converting total units into larger blocks.

```python
# 1. Calculating full groups / batches
total_items = 23
items_per_page = 5
full_pages = total_items // items_per_page
print(f"Full pages: {full_pages}")  # Full pages: 4

# 2. Converting seconds into hours, minutes, and remaining seconds
total_seconds = 3725
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours}h {minutes}m {seconds}s")  # 1h 2m 5s
```
### Shortcut (Compound Assignment) Operators in Python

Shortcut operators—officially called **compound assignment operators**—combine an arithmetic operation with variable assignment in a single step, making code shorter and less repetitive.

#### How Shortcut Operators Work
- **Shorthand Pattern:** `x += 5` is shorthand for `x = x + 5` (the variable on the left is updated using its current value and the right-hand expression).
- **Common Arithmetic Shortcuts:** `+=` (add), `-=` (subtract), `*=` (multiply), `/=` (divide into `float`), `//=` (floor divide), `%=` (modulo remainder), and `**=` (exponentiate).
- **Readability & Safety:** Great for counters, accumulators, and running totals, though keeping expressions simple avoids surprises when types change (for example, `/=` always produces a `float`).

```python
x = 10

x += 5    # x = 10 + 5   -> 15
x -= 3    # x = 15 - 3   -> 12
x *= 2    # x = 12 * 2   -> 24
x //= 5   # x = 24 // 5  -> 4
x **= 3   # x = 4 ** 3   -> 64
x %= 10   # x = 64 % 10  -> 4
x /= 2    # x = 4 / 2    -> 2.0 (float)

print(x)  # 2.0
```

#### Practical Example: Tracking Score & Remaining Attempts
Shortcut operators shine when updating counters, totals, or remaining budgets inside loops and functions.

```python
# 1. Accumulating points across rounds
total_score = 0
round_points = [15, 25, 10]

for points in round_points:
    total_score += points

print(f"Final score: {total_score}")  # Final score: 50

# 2. Counting down remaining retries
retries_left = 3
while retries_left > 0:
    print(f"Attempting connection... ({retries_left} retries left)")
    retries_left -= 1
```
### Unary Operators in Python

A **unary operator** operates on a single operand (value or variable) rather than two. In Python, the main unary operators are unary minus (`-`), unary plus (`+`), bitwise NOT (`~`), and logical `not`.

#### Main Unary Operators
- **Unary Minus (`-`):** Flips the sign of a numeric value (positive to negative or negative to positive).
- **Unary Plus (`+`):** Explicitly denotes a positive number; for standard numbers it leaves the value unchanged (and can also convert certain objects/arrays depending on type).
- **Bitwise NOT (`~`):** Inverts every bit of an integer using two's complement arithmetic (`~x` evaluates to `-(x + 1)`).
- **Logical `not`:** Returns the opposite Boolean value (`True` becomes `False`, `False` becomes `True`, or evaluates truthiness of any object).

```python
x = 10
y = -4
is_ready = True

# Unary minus and unary plus
print(-x)        # -10
print(-y)        # 4
print(+x)        # 10
print(+y)        # -4

# Bitwise NOT (~x == -(x + 1))
print(~x)        # -11
print(~y)        # 3

# Logical not
print(not is_ready)  # False
print(not 0)         # True
print(not "text")    # False
```

#### Practical Example: Toggling State & Inverting Temperature/Balance Deltas
Unary operators are handy for flipping Boolean flags, reversing direction/change signs, or toggling states cleanly.

```python
# 1. Toggling a feature flag or mode
dark_mode = False
dark_mode = not dark_mode
print(f"Dark mode enabled: {dark_mode}")  # Dark mode enabled: True

# 2. Reversing a movement or net change value
net_change = 12.5
reversed_change = -net_change
print(f"Reversed change: {reversed_change}")  # Reversed change: -12.5
```
### Operator Precedence in Python

**Operator precedence** determines the order in which Python evaluates operators in an expression when multiple operators appear together. Higher-precedence operators run before lower-precedence ones unless overridden by parentheses `()`.

#### Precedence Order (Highest to Lowest — Common Operators)
1. **Parentheses `()`:** Always evaluated first—use parentheses to make order explicit and readable.
2. **Exponentiation `**`:** Evaluated before multiplication/division, and associates **right-to-left** (e.g., `2 ** 3 ** 2` means `2 ** (3 ** 2)` = `512`).
3. **Unary `+x`, `-x`, `~x`:** Sign and bitwise NOT operators.
4. **Multiplicative `*`, `/`, `//`, `%`:** Evaluated **left-to-right** at equal precedence.
5. **Additive `+`, `-`:** Evaluated **left-to-right** after multiplicative operators.
6. **Comparison `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in`:** Evaluated after arithmetic.
7. **Logical `not`, then `and`, then `or`:** `not` binds tightest among logical operators, followed by `and`, then `or`.

```python
# 1. Exponentiation (**) and right-to-left associativity
print(2 ** 3 ** 2)        # 512  -> 2 ** (3 ** 2) = 2 ** 9

# 2. Multiplicative (*, /, //, %) vs. Additive (+, -)
print(10 + 2 * 3)         # 16   -> 10 + (2 * 3)
print((10 + 2) * 3)       # 36   -> parentheses override precedence
print(20 - 10 // 4 * 2)   # 16   -> 20 - ((10 // 4) * 2) = 20 - (2 * 2)

# 3. Logical precedence: not -> and -> or
is_admin = False
is_staff = True
is_suspended = False

can_access = is_admin or is_staff and not is_suspended
print(can_access)         # True -> False or (True and (not False)) = True
```

#### Practical Example: Discount & Eligibility Calculation
Parentheses clarify intent so readers and teammates do not have to guess how arithmetic and boolean conditions group together.

```python
base_price = 100
discount_rate = 0.2
item_count = 3
has_coupon = True

# Clear grouping with parentheses
final_total = (base_price * item_count) * (1 - discount_rate)
qualifies_for_bonus = has_coupon and (final_total >= 200)

print(f"Final total: {final_total}")                # Final total: 240.0
print(f"Qualifies for bonus: {qualifies_for_bonus}")  # Qualifies for bonus: True
```
### Bitwise Operators in Programming

**Bitwise operators** manipulate numbers at the binary bit level (`0` and `1`). They are commonly used for feature flags/permissions, bitmasks, low-level hardware/protocol work, and fast powers-of-two shifts.

#### Core Bitwise Operators
- **Bitwise AND (`&`):** Returns `1` in each bit position where **both** operands have `1` (useful for masking/checking bits).
- **Bitwise OR (`|`):** Returns `1` in each bit position where **at least one** operand has `1` (useful for setting/enabling flags).
- **Bitwise XOR (`^`):** Returns `1` where the bits of the two operands **differ** (useful for toggling bits).
- **Bitwise NOT (`~`):** Inverts all bits of an integer; in Python's two's complement representation, `~x` equals `-(x + 1)`.
- **Left Shift (`<<`):** Shifts bits left by `n` positions, filling right positions with `0` (equivalent to multiplying by $2^n$ for non-negative integers).
- **Right Shift (`>>`):** Shifts bits right by `n` positions, discarding shifted-out bits (equivalent to floor-dividing by $2^n$ for non-negative integers).

```python
a = 0b1100  # 12 in decimal
b = 0b1010  # 10 in decimal

print(bin(a & b), a & b)    # 0b1000  8   (AND)
print(bin(a | b), a | b)    # 0b1110  14  (OR)
print(bin(a ^ b), a ^ b)    # 0b110   6   (XOR)
print(~a)                   # -13         (NOT: -(12 + 1))
print(bin(a << 1), a << 1)  # 0b11000 24  (12 * 2^1)
print(bin(a >> 1), a >> 1)  # 0b110   6   (12 // 2^1)
```

#### Practical Example: Permission Flags & Bitmasks
Bitwise OR (`|`), AND (`&`), and XOR (`^`) make it clean to combine, check, and toggle individual boolean permissions inside a single integer.

```python
READ = 0b001    # 1
WRITE = 0b010   # 2
EXECUTE = 0b100 # 4

# Grant READ and WRITE permissions using OR (|)
permissions = READ | WRITE
print(f"Permissions binary: {bin(permissions)}")  # 0b11 (3)

# Check if WRITE permission is set using AND (&)
can_write = (permissions & WRITE) != 0
print(f"Can write: {can_write}")                  # True

# Toggle EXECUTE permission using XOR (^)
permissions ^= EXECUTE
print(f"After toggling execute: {bin(permissions)}")  # 0b111 (7)
```
<h2>Python Boolean Operators</h2>

<p>Boolean operators in Python are used to combine conditional statements and evaluate expressions to either <code>True</code> or <code>False</code>. Python has three primary logical operators: <code>and</code>, <code>or</code>, and <code>not</code>.</p>

<h3>1. Overview &amp; Precedence</h3>
<p>When multiple boolean operators appear in a single expression, Python evaluates them in the following order of precedence (from highest to lowest):</p>
<ol>
  <li><code>not</code></li>
  <li><code>and</code></li>
  <li><code>or</code></li>
</ol>

<table>
  <thead>
    <tr>
      <th>Operator</th>
      <th>Description</th>
      <th>Example</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>and</code></td>
      <td>Returns <code>True</code> if <strong>both</strong> statements are true</td>
      <td><code>True and False</code></td>
      <td><code>False</code></td>
    </tr>
    <tr>
      <td><code>or</code></td>
      <td>Returns <code>True</code> if <strong>at least one</strong> statement is true</td>
      <td><code>True or False</code></td>
      <td><code>True</code></td>
    </tr>
    <tr>
      <td><code>not</code></td>
      <td>Reverses the result; returns <code>False</code> if the result is true</td>
      <td><code>not True</code></td>
      <td><code>False</code></td>
    </tr>
  </tbody>
</table>

<h3>2. Truth Tables</h3>

<h4><code>and</code> Operator</h4>
<table>
  <thead>
    <tr>
      <th>A</th>
      <th>B</th>
      <th>A <code>and</code> B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>True</code></td>
      <td><code>True</code></td>
      <td><code>True</code></td>
    </tr>
    <tr>
      <td><code>True</code></td>
      <td><code>False</code></td>
      <td><code>False</code></td>
    </tr>
    <tr>
      <td><code>False</code></td>
      <td><code>True</code></td>
      <td><code>False</code></td>
    </tr>
    <tr>
      <td><code>False</code></td>
      <td><code>False</code></td>
      <td><code>False</code></td>
    </tr>
  </tbody>
</table>

<h4><code>or</code> Operator</h4>
<table>
  <thead>
    <tr>
      <th>A</th>
      <th>B</th>
      <th>A <code>or</code> B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>True</code></td>
      <td><code>True</code></td>
      <td><code>True</code></td>
    </tr>
    <tr>
      <td><code>True</code></td>
      <td><code>False</code></td>
      <td><code>True</code></td>
    </tr>
    <tr>
      <td><code>False</code></td>
      <td><code>True</code></td>
      <td><code>True</code></td>
    </tr>
    <tr>
      <td><code>False</code></td>
      <td><code>False</code></td>
      <td><code>False</code></td>
    </tr>
  </tbody>
</table>

<h4><code>not</code> Operator</h4>
<table>
  <thead>
    <tr>
      <th>A</th>
      <th><code>not</code> A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>True</code></td>
      <td><code>False</code></td>
    </tr>
    <tr>
      <td><code>False</code></td>
      <td><code>True</code></td>
    </tr>
  </tbody>
</table>

<h3>3. Code Examples</h3>
<pre><code class="language-python">x = 10
y = 5

# and operator
print(x &gt; 5 and y &lt; 10)   # True

# or operator
print(x &lt; 5 or y &lt; 10)    # True

# not operator
print(not(x &gt; 5))         # False

# Combining operators (precedence: not -&gt; and -&gt; or)
print(True or False and False)  # True (evaluated as: True or (False and False))
</code></pre>

<h3>4. Short-Circuit Evaluation &amp; Truthiness</h3>
<ul>
  <li><strong>Short-Circuiting:</strong> Python stops evaluating as soon as the outcome is determined. In <code>A and B</code>, if <code>A</code> is falsy, <code>B</code> is never evaluated. In <code>A or B</code>, if <code>A</code> is truthy, <code>B</code> is never evaluated.</li>
  <li><strong>Return Values:</strong> <code>and</code> and <code>or</code> actually return one of their operands rather than strictly <code>True</code> or <code>False</code> (e.g., <code>0 or "default"</code> returns <code>"default"</code>).</li>
  <li><strong>Falsy Values in Python:</strong> <code>False</code>, <code>None</code>, <code>0</code>, <code>0.0</code>, <code>""</code> (empty string), <code>[]</code>, <code>()</code>, <code>{}</code>, and <code>set()</code>. Everything else is truthy.</li>
</ul>
<h1>Python Boolean Expressions &amp; Eligibility Logic</h1>

<p>Boolean expressions are used to evaluate conditions that control the flow of Python programs. They are essential for implementing logic, such as determining if a user is eligible for a discount, checking number ranges, or combining multiple criteria.</p>

<hr>

<h2>1. Checking User Eligibility with Boolean Expressions</h2>
<p>Boolean expressions evaluate whether a specific situation is occurring (<code>True</code> or <code>False</code>) to determine follow-up actions.</p>

<h3>Example Breakdown</h3>
<ul>
  <li><strong>Criteria:</strong> The user qualifies for a discount if they have spent more than $100 <strong>or</strong> are a loyalty program member.</li>
  <li><strong>Logical <code>or</code> Operator:</strong> The user qualifies if <em>either</em> condition is true.</li>
</ul>

<pre><code class="language-python"># Variable Initialization
total_spent = 120.50
is_loyalty_member = False

# Eligibility Check
qualifies_for_discount = total_spent > 100 or is_loyalty_member

# Output
print(f"User qualifies for discount: {qualifies_for_discount}")
</code></pre>

<p><strong>Output:</strong></p>
<pre><code class="language-text">User qualifies for discount: True
</code></pre>

<blockquote>
  <strong>How It Works:</strong> <code>total_spent &gt; 100</code> evaluates to <code>True</code>, and <code>is_loyalty_member</code> evaluates to <code>False</code>. Because the <code>or</code> operator only requires one condition to be true, the final result is <code>True</code>.
</blockquote>

<hr>

<h2>2. Checking Number Ranges with Boolean Expressions</h2>
<p>You can combine comparison operators to verify if a numeric value lies within a specific inclusive range.</p>

<h3>Example Breakdown</h3>
<ul>
  <li><strong>Criteria:</strong> Users must be between 18 and 65 years old (inclusive) to qualify for the program.</li>
  <li><strong>Logical <code>and</code> Operator:</strong> Connects both conditions, making eligibility <code>True</code> only if <em>both</em> boundaries are satisfied.</li>
</ul>

<pre><code class="language-python"># Define the Variable
age = 25

# Write the Eligibility Check
is_eligible = (age >= 18) and (age <= 65)

# Print the Result
print(f"User is eligible: {is_eligible}")
</code></pre>

<p><strong>Output:</strong></p>
<pre><code class="language-text">User is eligible: True
</code></pre>

<blockquote>
  <strong>How It Works:</strong> <code>(age &gt;= 18)</code> confirms the user is 18 or older, while <code>(age &lt;= 65)</code> confirms they are 65 or younger. Both are <code>True</code> for age 25.
</blockquote>

<hr>

<h2>3. Combining Boolean Conditions for Senior Discount Eligibility</h2>
<p>Boolean expressions can evaluate completely different data types (like numbers and booleans) simultaneously.</p>

<h3>Example Breakdown</h3>
<ul>
  <li><strong>Criteria:</strong> The user is eligible for a senior discount if they are 65 or older <strong>and</strong> possess a valid membership card.</li>
</ul>

<pre><code class="language-python"># Variable Initialization
age = 70
has_membership_card = True

# Eligibility Check
qualifies_for_senior_discount = (age >= 65) and has_membership_card

# Output
print(f"User qualifies for senior discount: {qualifies_for_senior_discount}")
</code></pre>

<p><strong>Output:</strong></p>
<pre><code class="language-text">User qualifies for senior discount: True
</code></pre>

<hr>

<h2>4. Nested Boolean Expressions for Special Offers</h2>
<p>Parentheses allow you to group and nest Boolean expressions to build complex, multi-factor qualification rules.</p>

<h3>Variables &amp; Conditions</h3>
<ul>
  <li><strong>Age Check:</strong> Must be between 18 and 30 (<code>age &gt;= 18 and age &lt;= 30</code>).</li>
  <li><strong>Spending or Membership Check:</strong> Must exceed $100 <em>or</em> be a loyalty member (<code>total_spent &gt; 100 or loyalty_member</code>).</li>
  <li><strong>Combined Rule:</strong> Both primary groups must evaluate to <code>True</code> using the <code>and</code> operator.</li>
</ul>

<pre><code class="language-python"># Define Variables
age = 30
total_spent = 150.75
loyalty_member = True

# Nested Conditions
qualifies_for_offer = (age >= 18 and age <= 30) and (total_spent > 100 or loyalty_member)

# Output
print(f"User qualifies for special offer: {qualifies_for_offer}")
</code></pre>

<p><strong>Output:</strong></p>
<pre><code class="language-text">User qualifies for special offer: True
</code></pre>

<hr>

<h2>Quiz Question</h2>
<p>What will the following Python code output?</p>

<pre><code class="language-python">a = 10
b = 7
print(a >= b)
</code></pre>

<details>
  <summary><strong>Click to reveal answer</strong></summary>
  <p><strong>Output:</strong> <code>True</code></p>
  <p><strong>Explanation:</strong> The <code>&gt;=</code> operator checks if <code>a</code> is greater than or equal to <code>b</code>. Since <code>10</code> is greater than <code>7</code>, the expression evaluates to <code>True</code>.</p>
</details>
