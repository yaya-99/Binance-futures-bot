# Binance Futures Trading Bot 🤖

A simplified yet powerful trading bot for Binance **USDT-M Futures Testnet**, built using the official `python-binance` library. It supports market and limit orders via both:

- ✅ Command-line interface (CLI) with `prompt_toolkit` and `rich`
- ✅ Lightweight web UI using Streamlit

---

## 🚀 Features

- 🔐 Connect securely using API Key & Secret
- 🟢 Place Market & Limit Orders (BUY/SELL)
- 📈 Streamlit Web Interface for ease of use
- 💻 Rich CLI with autocomplete, input validation, and colorful output
- 🧠 Structured logging and error handling
- ⚙️ Easily extensible to support Stop-Limit, OCO, and Grid strategies

---

## 📦 Installation

```bash
git clone https://github.com/yaya-99/Binance-futures-bot.git
cd Binance-futures-bot

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Using the Binance Futures Testnet

1. Register at: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
2. Create API Keys from the API Management tab
3. Add test USDT in your testnet wallet

---

## 🖥️ CLI Usage

```bash
python cli.py
```

- Input your API credentials when prompted
- Autocomplete available for order type and side
- Supports placing multiple orders in a single session

---

## 🌐 Web UI with Streamlit

```bash
streamlit run app.py
```

- Enter your API credentials
- Submit Market or Limit orders from the dashboard

---

## 📁 Project Structure

```
binance-futures-bot/
├── bot.py          # Core trading logic
├── cli.py          # CLI interface
├── app.py          # Streamlit web UI
├── requirements.txt
└── README.md
```

---

## 🔐 .env (Optional)

For easier API credential management, you can use a `.env` file:

```env
API_KEY=your_key
API_SECRET=your_secret
```

Then modify `bot.py` to use `dotenv` (not included by default):

```bash
pip install python-dotenv
```

```python
# At the top of bot.py
from dotenv import load_dotenv
load_dotenv()
import os

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
```

---

## 🛠️ Future Features

- ⏱️ Stop-Limit and OCO support
- 📊 Order history and trade results display
- 🤖 Strategy automation (TWAP, Grid)
- 🚨 Telegram or email alerts

---

## 📜 License

MIT License. Feel free to use and extend this bot for educational or research purposes.

---

## 🙋‍♂️ Author

Made by [@yaya-99](https://github.com/yaya-99) — contributions and stars are welcome!
