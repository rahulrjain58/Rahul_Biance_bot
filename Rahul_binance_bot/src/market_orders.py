from basic_bot import BasicBot

def place_market(symbol, side, quantity):
    bot = BasicBot()
    return bot.place_market_order(symbol, side, quantity)
