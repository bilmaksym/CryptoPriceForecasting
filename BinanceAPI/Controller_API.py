from BinanceAPI.BinanceAccountDataEndpoints import BinanceAccountDataEndpoints as bin_account
from BinanceAPI.BinanceGeneralEndpoints import BinanceGeneralEndpoints as bin_general
from BinanceAPI.BinanceFuturesEndpoints import BinanceFuturesAPI as bin_futures
from BinanceAPI.BinanceLendingEndpoints import BinanceLendingEndpoints as bin_lending
from BinanceAPI.BinanceMarginTradingEndpoints import BinanceMarginTradingEndpoints as bin_margin
from BinanceAPI.BinanceMarketDataEndpoints import BinanceMarketDataEndpoints as bin_market
from BinanceAPI.BinanceSubAccounts import BinanceSubAccounts as bin_sub_accounts
from BinanceAPI.BinanceUserStreamEndpoints import BinanceUserStreamEndpoints as bin_user_stream
from BinanceAPI.BinanceWithdrawEndpoints import BinanceWithdrawEndpoints as bin_withdraw


class Controller:
    """
        This class is controlling all wrappers for Binance API
    """

    def __init__(self, API_KEY, API_SECRET, requests_params=None):
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET
        self.requests_params = requests_params

    def account_data_endpoints(self):
        return bin_account(self.API_KEY, self.API_SECRET, requests_params=self.requests_params)

    def general_data_endpoints(self):
        return bin_general(self.API_KEY, self.API_SECRET, requests_params=self.requests_params)

    def futures_trading(self):
        return bin_futures(self.API_KEY, self.API_SECRET, requests_params=self.requests_params)

    def lending_endpoints(self):
        return bin_lending(self.API_KEY, self.API_SECRET, requests_params=self.requests_params)

    def margin_trading(self):
        return bin_margin(self.API_KEY, self.API_SECRET, requests_params=self.requests_params)

    def market_data_endpoints(self):
        return bin_market(self.API_KEY, self.API_SECRET, requests_params=self.requests_params)

    def sub_accounts(self):
        return bin_sub_accounts(self.API_KEY, self.API_SECRET, requests_params=self.requests_params)

    def user_stream_endpoints(self):
        return bin_user_stream(self.API_KEY, self.API_SECRET, requests_params=self.requests_params)

    def withdraw_endpoints(self):
        return bin_withdraw(self.API_KEY, self.API_SECRET, requests_params=self.requests_params)
