from .client import Client


class BinanceUserStreamEndpoints:
    """
        Wrapper for User Stream Endpoints
    """

    def __init__(self, api_key=None, api_secret=None, requests_params=None, tld='com'):
        self.binance_call = Client(api_key, api_secret, requests_params, tld)

    def get_account(self, **params):
        """
        Get current account information.

        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.get_account(**params)

    def get_asset_balance(self, asset, **params):
        """
        Get current asset balance.

        :param asset: required
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: dictionary or None if not found
        """
        return self.binance_call.get_asset_balance(asset, **params)

    def get_my_trades(self, **params):
        """
        Get trades for a specific symbol.

        :param symbol: required
        :param limit: Default 500; max 500.
        :param fromId: TradeId to fetch from. Default gets most recent trades.
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.get_my_trades(**params)

    def get_system_status(self):
        """
        Get system status detail.

        :returns: API response
        """
        return self.binance_call.get_system_status()

    def get_account_status(self, **params):
        """
        Get account status detail.

        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.get_account_status(**params)

    def get_dust_log(self, **params):
        """
        Get log of small amounts exchanged for BNB.

        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.get_dust_log(**params)

    def transfer_dust(self, **params):
        """
        Convert dust assets to BNB.

        :param asset: The asset being converted. e.g: 'ONE'
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.transfer_dust(**params)

    def get_asset_dividend_history(self, **params):
        """
        Query asset dividend record.

        :param asset: optional
        :param startTime: optional
        :param endTime: optional
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.get_asset_dividend_history(**params)

    def get_trade_fee(self, **params):
        """
        Get trade fee.

        :param symbol: optional
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.get_trade_fee(**params)

    def get_asset_details(self, **params):
        """
        Fetch details on assets.

        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.get_asset_details(**params)

    def stream_get_listen_key(self):
        """
        Start a new user data stream and return the listen key
        If a stream already exists it should return the same key.
        If the stream becomes invalid a new key is returned.

        Can be used to keep the user stream alive.

        :returns: API response
        """
        return self.binance_call.margin_stream_get_listen_key()

    def stream_keepalive(self, listenKey):
        """
        PING a user data stream to prevent a time out.

        :param listenKey: required

        :returns: API response
        """
        return self.binance_call.stream_keepalive(listenKey)

    def stream_close(self, listenKey):
        """
        Close out a user data stream.

        :param listenKey: required

        :returns: API response
        """
        return self.binance_call.stream_close(listenKey)

