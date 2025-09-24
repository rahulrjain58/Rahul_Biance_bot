import argparse
from market_orders import place_market
from limit_orders import place_limit
from stop_orders import place_stop

def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Market order
    market_parser = subparsers.add_parser("market")
    market_parser.add_argument("--symbol", required=True)
    market_parser.add_argument("--side", required=True, choices=["BUY","SELL"])
    market_parser.add_argument("--quantity", type=float, required=True)

    # Limit order
    limit_parser = subparsers.add_parser("limit")
    limit_parser.add_argument("--symbol", required=True)
    limit_parser.add_argument("--side", required=True, choices=["BUY","SELL"])
    limit_parser.add_argument("--quantity", type=float, required=True)
    limit_parser.add_argument("--price", type=float, required=True)

    # Stop-Limit order
    stop_parser = subparsers.add_parser("stop")
    stop_parser.add_argument("--symbol", required=True)
    stop_parser.add_argument("--side", required=True, choices=["BUY","SELL"])
    stop_parser.add_argument("--quantity", type=float, required=True)
    stop_parser.add_argument("--stopPrice", type=float, required=True)
    stop_parser.add_argument("--limitPrice", type=float, required=True)

    args = parser.parse_args()

    if args.command == "market":
        result = place_market(args.symbol, args.side, args.quantity)
    elif args.command == "limit":
        result = place_limit(args.symbol, args.side, args.quantity, args.price)
    elif args.command == "stop":
        result = place_stop(args.symbol, args.side, args.quantity, args.stopPrice, args.limitPrice)
    else:
        parser.print_help()
        return

    print("Result:", result)

if __name__ == "__main__":
    main()
