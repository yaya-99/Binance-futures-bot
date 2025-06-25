# bot.py
from binance.client import Client
from binance.enums import *
import logging

logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        try:
            self.client.futures_account()
            logging.info("Connected to Binance Futures Testnet")
        except Exception as e:
            logging.error(f"Failed to connect: {e}")
            raise

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            side_enum = SIDE_BUY if side == 'BUY' else SIDE_SELL
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            else:
                raise ValueError("Unsupported order type")

            logging.info(f"Order successful: {order}")
            return order

        except Exception as e:
            logging.error(f"Order error: {e}")
            return None

    def get_balance(self):
        try:
            return self.client.futures_account_balance()
        except Exception as e:
            logging.error(f"Error getting balance: {e}")
            return None
