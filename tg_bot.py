#TOKEN = "6965379630:AAGv7cC9A7a6EyqoQ6_J46hgUgkRkVbm7cY"

from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests

TOKEN = "6965379630:AAGv7cC9A7a6EyqoQ6_J46hgUgkRkVbm7cY"

CRYPTO_NAME_TO_TICKER = {
    "Bitcoin": "BITUSDT",
    "Ethereum": "ETHUSDT",
    "Doge": "DOGEUSDT"
}

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_message(message):
    markup = ReplyKeyboardMarkup(row_width=3)
    for crypto_name in CRYPTO_NAME_TO_TICKER.keys():
        item_button = KeyboardButton(crypto_name)
        markup.add(item_button)
    bot.send_message(message.chat.id, text="Выберите криптовалюту", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in CRYPTO_NAME_TO_TICKER.keys())
def send_price(message):
    crypto_name = message.text
    ticker = CRYPTO_NAME_TO_TICKER[crypto_name]
    price = get_price_by_ticker(ticker)
    bot.send_message(message.chat.id, text=f"Цена {crypto_name} в $ = {price}")

def get_price_by_ticker(ticker: str) -> float:
    endpoint = "https://api.binance.com/api/v3/ticker/price"
    params = {
        'symbol': ticker,
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    price = round(float(data["price"]), 2)
    return price

bot.polling(non_stop=True)