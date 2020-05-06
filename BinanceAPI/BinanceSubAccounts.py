from .client import Client


class BinanceSubAccounts:
    """
        Wrapper for Sub Accounts API
    """

    def __init__(self, api_key=None, api_secret=None, requests_params=None, tld='com'):
        self.binance_call = Client(api_key, api_secret, requests_params, tld)

    def get_sub_account_list(self, **params):
        """
        Query Sub-account List.

        :param email: optional
        :param startTime: optional
        :param endTime: optional
        :param page: optional
        :param limit: optional
        :param recvWindow: optional

        :returns: API response
        """
        return self.binance_call.get_sub_account_list(**params)

    def get_sub_account_transfer_history(self, **params):
        """
        Query Sub-account Transfer History.

        :param email: required
        :param startTime: optional
        :param endTime: optional
        :param page: optional
        :param limit: optional
        :param recvWindow: optional

        :returns: API response
        """
        return self.binance_call.get_sub_account_transfer_history(**params)

    def create_sub_account_transfer(self, **params):
        """
        Execute sub-account transfer

        :param fromEmail: required - Sender email
        :param toEmail: required - Recipient email
        :param asset: required
        :param amount: required
        :param recvWindow: optional

        :returns: API response
        """
        return self.binance_call.create_sub_account_transfer(**params)

    def get_sub_account_assets(self, **params):
        """
        Fetch sub-account assets

        :param email: required
        :param symbol: optional
        :param recvWindow: optional

        :returns: API response
        """
        return self.binance_call.get_sub_account_assets(**params)