import argparse

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.orders import place_market_order, place_limit_order
from bot.logging_config import setup_logger

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--qty", required=True, help="Order quantity")
    parser.add_argument("--price", help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # Validate inputs
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.qty)
        price = validate_price(args.price, order_type)

        print("\nOrder Request")
        print("-------------")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if price:
            print(f"Price: {price}")

        # Execute order
        if order_type == "MARKET":
            order = place_market_order(symbol, side, quantity)

        elif order_type == "LIMIT":
            order = place_limit_order(symbol, side, quantity, price)

        print("\nOrder Response")
        print("--------------")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice')}")

        print("\nSUCCESS: Order executed successfully")

    except Exception as e:
        logger.error(str(e))
        print(f"\nERROR: {str(e)}")


if __name__ == "__main__":
    main()