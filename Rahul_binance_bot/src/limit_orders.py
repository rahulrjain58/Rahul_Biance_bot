from basic_bot import BasicBot

def place_limit(symbol, side, quantity, price):
    bot = BasicBot()
    return bot.place_limit_order(symbol, side, quantity, price)
