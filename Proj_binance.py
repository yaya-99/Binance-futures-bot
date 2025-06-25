from binance.client import Client
from binance.enums import *
import logging
import os

# Configure logging
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
            # Validate connectivity
            status = self.client.futures_account()
            logging.info("Connected successfully to Binance Futures Testnet.")
        except Exception as e:
            logging.error(f"Connection failed: {e}")
            raise

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            else:
                raise ValueError("Unsupported order type")

            logging.info(f"Order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing order: {e}")
            return None

    def get_account_info(self):
        return self.client.futures_account_balance()

# ---- CLI Input Interface ---- #
def main():
    import getpass

    print("Welcome to the Binance Futures Testnet Bot\n")

    # Secure input (or use environment variables for automation)
    api_key = getpass.getpass("Enter your API Key: ")
    api_secret = getpass.getpass("Enter your API Secret: ")

    bot = BasicBot(api_key, api_secret)

    while True:
        try:
            symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
            side = input("Enter side (BUY/SELL): ").strip().upper()
            order_type = input("Order type (MARKET/LIMIT): ").strip().upper()
            quantity = float(input("Enter quantity: "))

            if order_type == 'LIMIT':
                price = float(input("Enter limit price: "))
            else:
                price = None

            order = bot.place_order(symbol, side, order_type, quantity, price)
            if order:
                print("Order placed successfully:", order['orderId'])
            else:
                print("Order failed. Check logs.")
        except Exception as e:
            logging.error(f"CLI input error: {e}")
            print(f"Error: {e}")

        again = input("Place another order? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()





