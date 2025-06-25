# cli.py
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from rich import print
from rich.table import Table
from bot import BasicBot

def enhanced_cli():
    import getpass

    print("[bold blue]Welcome to Binance Futures CLI Bot[/bold blue]")
    api_key = getpass.getpass("Enter API Key: ")
    api_secret = getpass.getpass("Enter API Secret: ")

    try:
        bot = BasicBot(api_key, api_secret)
    except:
        print("[red]Failed to initialize bot. Check API credentials.[/red]")
        return

    order_type_completer = WordCompleter(['MARKET', 'LIMIT'], ignore_case=True)
    side_completer = WordCompleter(['BUY', 'SELL'], ignore_case=True)

    while True:
        try:
            symbol = prompt("Symbol (e.g., BTCUSDT): ").upper()
            side = prompt("Side (BUY/SELL): ", completer=side_completer).upper()
            order_type = prompt("Order Type (MARKET/LIMIT): ", completer=order_type_completer).upper()
            quantity = float(prompt("Quantity: "))

            price = None
            if order_type == 'LIMIT':
                price = float(prompt("Limit Price: "))

            result = bot.place_order(symbol, side, order_type, quantity, price)

            if result:
                print("[green]Order Placed Successfully![/green]")
                table = Table(title="Order Summary")
                for key in ['orderId', 'symbol', 'side', 'type', 'status']:
                    table.add_row(key, str(result.get(key, 'N/A')))
                print(table)
            else:
                print("[red]Order failed. Check trading_bot.log[/red]")

        except Exception as e:
            print(f"[red]Error: {e}[/red]")

        again = prompt("Place another order? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    enhanced_cli()
