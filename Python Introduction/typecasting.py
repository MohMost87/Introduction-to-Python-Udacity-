from decimal import Decimal

# 1. String to int / float / Decimal
age_input = "25"
price_input = "19.90"

age = int(age_input)              # 25 (int)
price_float = float(price_input)  # 19.9 (float)
price_dec = Decimal(price_input)  # Decimal('19.90') (exact decimal)

print(age + 5)                    # 30
print(price_dec * 2)              # Decimal('39.80')

# 2. Float to int (truncates toward zero, does not round)
score = 9.95
print(int(score))                 # 9
print(int(-9.95))                # -9

# 3. Numbers to string (for concatenation or formatting)
items_count = 3
total = Decimal("29.10")

message = "You bought " + str(items_count) + " items for $" + str(total)
print(message)                    # You bought 3 items for $29.10

# 4. Converting to bool (truthiness)
print(bool(0))                    # False
print(bool(42))                   # True
print(bool(""))                   # False
print(bool("False"))                # True (non-empty string is True!)
print(bool([]))                   # False
print(bool([1, 2]))               # True