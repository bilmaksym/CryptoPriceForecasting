from .client import Client


class BinanceFuturesAPI:
    """
        Wrapper for Futures API
    """

    def __init__(self, api_key=None, api_secret=None, requests_params=None, tld='com'):
        self.binance_call = Client(api_key, api_secret, requests_params, tld)

    def futures_ping(self):
        """
        Test connectivity to the Rest API
        """
        return self.binance_call.futures_ping()

    def futures_time(self):
        """
        Test connectivity to the Rest API and get the current server time.
        """
        return self.binance_call.futures_time()

    def futures_exchange_info(self):
        """
        Current exchange trading rules and symbol information
        """
        return self.binance_call.futures_exchange_info()

    def futures_order_book(self, **params):
        """
        Get the Order Book for the market
        """
        return self.binance_call.futures_order_book(**params)

    def futures_recent_trades(self, **params):
        """
        Get recent trades (up to last 500).
        """
        return self.binance_call.futures_recent_trades(**params)

    def futures_historical_trades(self, **params):
        """
        Get older market historical trades.
        """
        return self.binance_call.futures_historical_trades(**params)

    def futures_aggregate_trades(self, **params):
        """
        Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same
        price will have the quantity aggregated.
        """
        return self.binance_call.futures_aggregate_trades(**params)

    def futures_klines(self, **params):
        """
        Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.
        """
        return self.binance_call.futures_klines(**params)

    def futures_mark_price(self, **params):
        """
        Get Mark Price and Funding Rate
        """
        return self.binance_call.futures_mark_price(**params)

    def futures_funding_rate(self, **params):
        """
        Get funding rate history
        """
        return self.binance_call.futures_funding_rate(**params)

    def futures_ticker(self, **params):
        """
        24 hour rolling window price change statistics.
        """
        return self.binance_call.futures_ticker(**params)

    def futures_symbol_ticker(self, **params):
        """
        Latest price for a symbol or symbols.
        """
        return self.binance_call.futures_symbol_ticker(**params)

    def futures_orderbook_ticker(self, **params):
        """
        Best price/qty on the order book for a symbol or symbols.
        """
        return self.binance_call.futures_orderbook_ticker(**params)

    def futures_liquidation_orders(self, **params):
        """
        Get all liquidation orders
        """
        return self.binance_call.futures_liquidation_orders(**params)

    def futures_open_interest(self, **params):
        """
        Get present open interest of a specific symbol.
        """
        return self.binance_call.futures_open_interest(**params)

    def futures_leverage_bracket(self, **params):
        """
        Notional and Leverage Brackets
        """
        return self.binance_call.futures_leverage_bracket(**params)

    def transfer_history(self, **params):
        """
        Get future account transaction history list
        """
        return self.binance_call.transfer_history(**params)

    def futures_create_order(self, **params):
        """
        Send in a new order.
        """
        return self.binance_call.futures_create_order(**params)

    def futures_get_order(self, **params):
        """
        Check an order's status.
        """
        return self.binance_call.futures_get_order(**params)

    def futures_get_open_orders(self, **params):
        """
        Get all open orders on a symbol.
        """
        return self.binance_call.futures_get_open_orders(**params)

    def futures_get_all_orders(self, **params):
        """
        Get all futures account orders; active, canceled, or filled.
        """
        return self.binance_call.futures_get_all_orders(**params)

    def futures_cancel_order(self, **params):
        """
        Cancel an active futures order.
        """
        return self.binance_call.futures_create_order(**params)

    def futures_cancel_all_open_orders(self, **params):
        """
        Cancel all open futures orders
        """
        return self.binance_call.futures_cancel_all_open_orders(**params)

    def futures_cancel_orders(self, **params):
        """
        Cancel multiple futures orders
        """
        return self.binance_call.futures_cancel_orders(**params)

    def futures_account_balance(self, **params):
        """
        Get futures account balance
        """
        return self.binance_call.futures_account_balance(**params)

    def futures_account(self, **params):
        """
        Get current account information.
        """
        return self.binance_call.futures_account(**params)

    def futures_change_leverage(self, **params):
        """
        Change user's initial leverage of specific symbol market
        """
        return self.binance_call.futures_change_leverage(**params)

    def futures_change_margin_type(self, **params):
        """
        Change the margin type for a symbol
        """
        return self.binance_call.futures_change_margin_type(**params)

    def futures_change_position_margin(self, **params):
        """
        Change the position margin for a symbol
        """
        return self.binance_call.futures_change_position_margin(**params)

    def futures_position_margin_history(self, **params):
        """
        Get position margin change history
        """
        return self.binance_call.futures_position_margin_history(**params)

    def futures_position_information(self, **params):
        """
        Get position information
        """
        return self.binance_call.futures_position_information(**params)

    def futures_account_trades(self, **params):
        """
        Get trades for the authenticated account and symbol.
        """
        return self.binance_call.futures_account_trades(**params)

    def futures_income_history(self, **params):
        """
        Get income history for authenticated account
        """
        return self.binance_call.futures_income_history(**params)
