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