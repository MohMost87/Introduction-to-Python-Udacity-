cart_total = 75.0
is_member = True
promo_code = ""  # Empty string evaluates to False (falsy)

# Boolean expression: free shipping if member with $50+ OR any cart with a non-empty promo code
free_shipping = (is_member and cart_total >= 50) or bool(promo_code)

print("Free shipping:", free_shipping)  # True

# Negating a full expression with parentheses
no_discount = not (is_member or bool(promo_code))
print("No discount:", no_discount)  # False


age = 70
has_membership = True
qualified_for_age = age >= 65 or has_membership

print (f"Qualified for senior discount: {qualified_for_age}")