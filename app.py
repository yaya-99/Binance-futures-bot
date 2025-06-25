# app.py
import streamlit as st
from bot import BasicBot

st.set_page_config(page_title="Binance Futures Bot", layout="centered")

st.title("Binance Futures Testnet Bot")

api_key = st.text_input("API Key", type="password")
api_secret = st.text_input("API Secret", type="password")

if api_key and api_secret:
    try:
        bot = BasicBot(api_key, api_secret)
        st.success("Connected to Binance Futures Testnet")
    except:
        st.error("Invalid credentials or connection error.")
        st.stop()

    symbol = st.text_input("Trading Symbol", value="BTCUSDT")
    side = st.selectbox("Side", ["BUY", "SELL"])
    order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
    quantity = st.number_input("Quantity", value=0.01, min_value=0.0001, step=0.001)

    price = None
    if order_type == "LIMIT":
        price = st.number_input("Limit Price", min_value=0.0)

    if st.button("Place Order"):
        result = bot.place_order(symbol, side, order_type, quantity, price)
        if result:
            st.success(f"Order placed successfully! ID: {result['orderId']}")
            st.json(result)
        else:
            st.error("Order failed. Check logs.")
