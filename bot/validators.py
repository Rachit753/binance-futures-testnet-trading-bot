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

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")

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
    if order_type in ["LIMIT", "STOP_LIMIT"]:
        if price is None:
            raise ValueError("Price is required for LIMIT or STOP_LIMIT orders")

        try:
            p = float(price)

            if p <= 0:
                raise ValueError("Price must be greater than 0")

            return p

        except ValueError:
            raise ValueError("Price must be a valid number")

    return None


def validate_stop_price(stop_price, order_type):
    if order_type == "STOP_LIMIT":
        if stop_price is None:
            raise ValueError("Stop price is required for STOP_LIMIT orders")

        try:
            sp = float(stop_price)

            if sp <= 0:
                raise ValueError("Stop price must be greater than 0")

            return sp

        except ValueError:
            raise ValueError("Stop price must be a valid number")

    return None