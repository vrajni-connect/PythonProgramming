def apply_discount(price, discount):
    """
    Apply a discount to a price.

    :param price: The original price.
    :param discount: The discount to apply (as a percentage).
    :return: The discounted price.
    """
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100.")
    
    discounted_price = price * (1 - discount / 100)
    return round(discounted_price, 2)
def flat_discount(price, discount_amount=50):
    """
    Apply a flat discount to a price.

    :param price: The original price.
    :param discount_amount: The flat discount amount to apply.
    :return: The discounted price.
    """
    if discount_amount < 0:
        raise ValueError("Discount amount must be non-negative.")
    
    discounted_price = price - discount_amount
    return round(max(discounted_price, 0), 2)