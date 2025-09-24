# Binance Futures Testnet Trading Bot

## Setup

1. Activate Conda environment:
   & "C:\Users\Win10\anaconda3\Scripts\activate.bat" tradingbot

2. Install dependencies:
   pip install -r requirements.txt

3. Add your Binance Testnet keys to .env:
   BINANCE_API_KEY=YOUR_KEY
   BINANCE_API_SECRET=YOUR_SECRET

## Run bot

- Market order:
  python src/cli.py market --symbol BTCUSDT --side BUY --quantity 0.001

- Limit order:
  python src/cli.py limit --symbol BTCUSDT --side SELL --quantity 0.001 --price 120000

- Stop-Limit order:
  python src/cli.py stop --symbol BTCUSDT --side SELL --quantity 0.001 --stopPrice 125000 --limitPrice 124500

## Logs
All API requests, responses, and errors are logged in `bot.log`.
