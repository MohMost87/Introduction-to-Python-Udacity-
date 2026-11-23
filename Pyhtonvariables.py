my_var = False
if my_var:
      print("hello")
else:
      print ("good bye")

"""  this is a multi-line comment  """
""" think of code as instruction that allow us to deal and continue to work with code"""

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
print(calculate_discount(100,True))