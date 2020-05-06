from .client import Client


class BinanceWithdrawEndpoints:
    """
        Wrapper for Withdraw Endpoints
    """

    def __init__(self, api_key=None, api_secret=None, requests_params=None, tld='com'):
        self.binance_call = Client(api_key, api_secret, requests_params, tld)

    def withdraw(self, **params):
        """
        Submit a withdraw request.

        Assumptions:

        - You must have Withdraw permissions enabled on your API key
        - You must have withdrawn to the address specified through the website and approved the transaction via email

        :param asset: required
        :param amount: required
        :param name: optional - Description of the address, default asset value passed will be used
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.withdraw(**params)

    def get_deposit_history(self, **params):
        """
        Fetch deposit history.

        :param asset: optional
        :param startTime: optional
        :param endTime: optional
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.get_deposit_history(**params)

    def get_withdraw_history(self, **params):
        """
        Fetch withdraw history.

        :param asset: optional
        :param startTime: optional
        :param endTime: optional
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.get_withdraw_history(**params)

    def get_deposit_address(self, **params):
        """
        Fetch a deposit address for a symbol

        :param asset: required
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.get_deposit_address(**params)