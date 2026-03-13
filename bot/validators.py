from bot.logging_config import setup_logger

logger = setup_logger()


def validate_symbol(symbol):
    if not symbol:
        raise ValueError("Symbol is required")

    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs are supported (example: BTCUSDT)")

    return symbol.upper()


def validate_side(side):
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type):
    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    return order_type


def validate_quantity(quantity):
    try:
        qty = float(quantity)

        if qty <= 0:
            raise ValueError("Quantity must be greater than 0")

        return qty

    except ValueError:
        raise ValueError("Quantity must be a valid number")


def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")

        try:
            p = float(price)

            if p <= 0:
                raise ValueError("Price must be greater than 0")

            return p

        except ValueError:
            raise ValueError("Price must be a valid number")

    return None