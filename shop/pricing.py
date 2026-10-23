def subtotal(items):
    """items: list of (price, quantity)."""
    return sum(price * qty for price, qty in items)


def apply_discount(total, percent):
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(total * (100 - percent) / 100, 2)
