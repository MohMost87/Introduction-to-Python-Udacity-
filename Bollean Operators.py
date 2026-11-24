age = 22
has_id = True

can_enter = (age >= 18) and has_id
print(can_enter)  # True

# Short-circuiting: if the first part is False, Python skips the second part
x = 0
result = (x != 0) and (10 / x > 2)
print(result)  # False (no ZeroDivisionError)


is_weekend = True
is_holiday = False

can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)  # True

# Using truthiness to provide a fallback value
user_input = ""
display_name = user_input or "Guest"
print(display_name)  # "Guest"


is_logged_in = False

if not is_logged_in:
    print("Please sign in.")  # Prints: Please sign in.

print(not (5 > 10))  # True