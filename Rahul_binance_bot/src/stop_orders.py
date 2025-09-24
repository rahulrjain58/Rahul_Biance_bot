from basic_bot import BasicBot

def place_stop(symbol, side, quantity, stopPrice, limitPrice):
    bot = BasicBot()
    return bot.place_stop_limit_order(symbol, side, quantity, stopPrice, limitPrice)
