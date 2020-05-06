from .client import Client

class BinanceGeneralEndpoints:

    def __init__(self, api_key=None, api_secret=None, requests_params=None, tld='com'):
        self.binance_call = Client(api_key, api_secret, requests_params, tld)

    def get_exchange_info(self):
        """
        Return rate limits and list of symbols
        """
        return self.binance_call.get_exchange_info()

    def get_symbol_info(self, symbol):
        """
        Return information about a symbol
        :param symbol: required e.g BNBBTC
        :returns: Dict if found, None if not
        """
        return self.binance_call.get_symbol_info(symbol)

    def ping(self):
        """
        Test connectivity to the Rest API.
        :return: Empty array
        """
        return self.binance_call.ping()

    def time(self):
        """
        Test connectivity to the Rest API and get the current server time.
        :return: Current server time
        """
        return self.binance_call.get_server_time()
