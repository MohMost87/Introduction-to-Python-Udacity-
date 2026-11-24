from decimal import Decimal, ROUND_HALF_UP, getcontext

# 1. Relational operators
a = 10
b = 5
print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("a > b :", a > b)   # True
print("a >= b:", a >= b)  # True
print("a < b :", a < b)   # False
print("a <= b:", a <= b)  # False

c = 5
print("b >= c:", b >= c)  # True
print("b <= c:", b <= c)  # True

# 2. Boolean expressions & eligibility logic
age = 25
total_spent = Decimal("120.50")
is_loyalty_member = False
has_membership_card = True

qualifies_for_discount = (total_spent > Decimal("100")) or is_loyalty_member
in_age_range = (age >= 18) and (age <= 65)
qualifies_for_senior_discount = (age >= 65) and has_membership_card
qualifies_for_special_offer = (18 <= age <= 30) and (
    total_spent > Decimal("100") or is_loyalty_member
)

print("Discount eligible:", qualifies_for_discount)
print("Age range (18-65):", in_age_range)
print("Senior discount:", qualifies_for_senior_discount)
print("Special offer:", qualifies_for_special_offer)

# 3. Float vs. Decimal precision
print("Float 0.1 + 0.2:", 0.1 + 0.2)  # 0.30000000000000004
print("Decimal 0.1 + 0.2:", Decimal("0.1") + Decimal("0.2"))  # 0.3

# 4. Price calculation, rounding, and formatting
items = [Decimal("19.90"), Decimal("5.70"), Decimal("3.50")]
subtotal = sum(items, Decimal("0.00"))
tax_rate = Decimal("0.08")
tax = (subtotal * tax_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
final_total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax     : ${tax:.2f}")
print(f"Total   : ${final_total:.2f}")

# 5. Testing getcontext().prec (total significant digits)
getcontext().prec = 3
print("prec=3 (1 / 3):", Decimal("1") / Decimal("3"))  # 0.333

getcontext().prec = 10
print("prec=10 (1 / 3):", Decimal("1") / Decimal("3"))  # 0.3333333333

# Restore default precision
getcontext().prec = 28