from binance.client import Client
from dotenv import load_dotenv
import os

from bot.logging_config import setup_logger

# Load environment variables
load_dotenv()

logger = setup_logger()


def create_client():
    try:
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_SECRET_KEY")

        if not api_key or not api_secret:
            raise ValueError("API keys not found in .env file")

        client = Client(api_key, api_secret)

        # Connect to Binance Futures Testnet
        client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Binance client initialized successfully")

        return client

    except Exception as e:
        logger.error(f"Error creating Binance client: {str(e)}")
        raise