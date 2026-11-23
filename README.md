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

