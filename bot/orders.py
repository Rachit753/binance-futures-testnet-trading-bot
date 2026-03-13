from bot.client import create_client
from bot.logging_config import setup_logger

logger = setup_logger()


def place_market_order(symbol, side, quantity):
    try:
        client = create_client()

        logger.info(f"Sending MARKET order | {symbol} {side} qty={quantity}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"Order response: {order}")

        return order

    except Exception as e:
        logger.error(f"Market order failed: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        client = create_client()

        logger.info(
            f"Sending LIMIT order | {symbol} {side} qty={quantity} price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Order response: {order}")

        return order

    except Exception as e:
        logger.error(f"Limit order failed: {str(e)}")
        raise


def place_stop_limit_order(symbol, side, quantity, price, stop_price):
    try:
        client = create_client()

        logger.info(
            f"Sending STOP_LIMIT order | {symbol} {side} qty={quantity} price={price} stop={stop_price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            price=price,
            stopPrice=stop_price,
            timeInForce="GTC"
        )

        logger.info(f"Order response: {order}")

        return order

    except Exception as e:
        logger.error(f"Stop-limit order failed: {str(e)}")
        raise