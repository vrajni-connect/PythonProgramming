def calculate_total(prices):
    """Calculate the total price from a list of prices."""
    return sum(prices)
def apply_tax(price, tax_rate=5):
    """Apply tax to a price."""
    if tax_rate < 0:
        raise ValueError("Tax rate must be non-negative.")
    
    taxed_price = price * (1 + tax_rate / 100)
    return round(taxed_price, 2)