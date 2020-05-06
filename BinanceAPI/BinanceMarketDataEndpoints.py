from .client import Client


class BinanceMarketDataEndpoints:
    """
        Wrapper for Market Data Endpoints
    """

    def __init__(self, api_key=None, api_secret=None, requests_params=None, tld='com'):
        self.binance_call = Client(api_key, api_secret, requests_params, tld)

    def get_all_tickers(self):
        """
        Latest price for all symbols
        :return: List of market tickers
        """
        return self.binance_call.get_all_tickers()

    def get_order_book_tickers(self):
        """
        Best price/qty on the order book for all symbols
        :return: List of order book market entries
        """
        return self.binance_call.get_orderbook_tickers()

    def get_order_book(self, **params):
        """
        Get the Order Book for the market
        :param params: symbol(required)- e.g. BNBBTC, limit(optional): by default 100, max - 1000+
        :return: API response
        """
        return self.binance_call.get_order_book(**params)

    def get_recent_trades(self, **params):
        """
        Get recent trades (up to last 500)
        :param params: symbol(required): e.g. BNBBTC, limit(optional): by default 500, max - 500
        :return: API response
        """
        return self.binance_call.get_recent_trades(**params)

    def get_historical_trades(self, **params):
        """
        Get older trades
        :param params: symbol(required): e.g. BNBBTC, limit(optional): by default 500, max - 500, fromId(optional): TradeId to fetch from. Default gets most recent trades.
        :return:
        """
        return self.binance_call.get_historical_trades(**params)

    def get_aggregate_trades(self, **params):
        """
        Get compressed, aggregate trades. Trades that fill at the time,
        from the same order, with the same price will have the quantity aggregated.
        :param params: symbol(required): e.g. BNBBTC,
        fromId(optional): ID to get aggregate trades from INCLUSIVE,
        startTime(optional): Timestamp in ms to get aggregate trades from INCLUSIVE,
        endTime(optional): Timestamp in ms to get aggregate trades until INCLUSIVE,
        limit(optional): by default 500, max - 500
        :return: API response
        """
        return self.binance_call.get_aggregate_trades(**params)

    def aggregate_trade_iter(self, symbol, start_str=None, last_id=None):
        """
        Iterate over aggregate trade data from (start_time or last_id) to
        the end of the history so far.

        If start_time is specified, start with the first trade after
        start_time. Meant to initialise a local cache of trade data.

        If last_id is specified, start with the trade after it. This is meant
        for updating a pre-existing local trade data cache.

        Only allows start_str or last_id—not both. Not guaranteed to work
        right if you're running more than one of these simultaneously. You
        will probably hit your rate limit.
        :param symbol: Symbol string e.g. BNBBTC
        :param start_str: Start date string in UTC format or timestamp in milliseconds. The iterator will
        return the first trade occurring later than this time.
        :param last_id: aggregate trade ID of the last known aggregate trade.
        Not a regular trade ID. See https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#compressedaggregate-trades-list.

        :return: an iterator of JSON objects, one per trade. The format of
        each object is identical to Client.aggregate_trades().
        """
        return self.binance_call.aggregate_trade_iter(symbol, start_str, last_id)

    def get_klines(self, **params):
        """
        Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.
        :param params: symbol(required): e.g. BNBBTC,
        interval(required): type -ENUM
        startTime(optional):
        endTime(optional):
        limit(optional): by default 500, max - 500
        :return: API response
        """
        return self.binance_call.get_klines(**params)

    def get_historical_klines(self, symbol, interval, start_str, end_str=None, limit=500):
        """
        Get Historical Klines from Binance
        :param symbol:e.g BNBBTC
        :param interval: Binance Kline interval
        :param start_str: Start date string in UTC format or timestamp in milliseconds
        :param end_str: optional - end date string in UTC format or timestamp in milliseconds (default will fetch everything up to now)
        :param limit: Default 500; max 1000.

        :return: list of OHLCV values
        """
        return self.binance_call.get_historical_klines(symbol, interval, start_str, end_str, limit)

    def get_historical_klines_generator(self, symbol, interval, start_str, end_str=None):
        """
        Get Historical Klines from Binance

        If using offset strings for dates add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"

        :param symbol: e.g BNBBTC
        :param interval: Binance Kline interval
        :param start_str: Start date string in UTC format or timestamp in milliseconds
        :param end_str: optional - end date string in UTC format or timestamp in milliseconds (default will fetch everything up to now)

        :return: generator of OHLCV values
        """
        return self.binance_call.get_historical_klines_generator(symbol, interval, start_str, end_str)

    def get_avg_price(self, **params):
        """
        Current average price for a symbol.

        symbol(required): e.g. BNBBTC

        :return: API response
        """
        return self.binance_call.get_avg_price(**params)

    def get_ticker(self, **params):
        """
        24 hour price change statistics.
        :param params: symbol(required): e.g. BNBBTC

        :return: API response
        """
        return self.binance_call.get_ticker(**params)

    def get_symbol_ticker(self, **params):
        """
        Latest price for a symbol or symbols.

        :param: symbol(required): e.g. BNBBTC

        :returns: API response
        """
        return self.binance_call.get_symbol_ticker(**params)

    def get_orderbook_ticker(self, **params):
        """
        Latest price for a symbol or symbols.

        :param symbol(required): e.g. BNBBTC

        :returns: API response
        """
        return self.binance_call.get_orderbook_ticker(**params)
