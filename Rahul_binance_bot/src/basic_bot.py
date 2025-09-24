import os
import logging
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Configure logging
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BasicBot:
    def __init__(self, api_key=None, api_secret=None, testnet=True):
        load_dotenv()
        api_key = api_key or os.getenv("BINANCE_API_KEY")
        api_secret = api_secret or os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API Key and Secret required. Check .env file.")

        self.client = Client(api_key, api_secret, testnet=testnet)
        self.client.API_URL = "https://testnet.binancefuture.com/fapi"

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol, side=side, type="MARKET", quantity=quantity
            )
            logging.info(f"Market order: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Market order error: {e}")
            return {"error": str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol, side=side, type="LIMIT",
                timeInForce="GTC", quantity=quantity, price=price
            )
            logging.info(f"Limit order: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Limit order error: {e}")
            return {"error": str(e)}

    def place_stop_limit_order(self, symbol, side, quantity, stopPrice, limitPrice):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                stopPrice=stopPrice,
                closePosition=False,
                quantity=quantity
            )
            logging.info(f"Stop-Limit order: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Stop-Limit order error: {e}")
            return {"error": str(e)}
