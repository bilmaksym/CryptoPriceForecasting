from .client import Client


class BinanceLendingEndpoints:
    """
        Wrapper for Lending Endpoints
    """

    def __init__(self, api_key=None, api_secret=None, requests_params=None, tld='com'):
        self.binance_call = Client(api_key, api_secret, requests_params, tld)

    def get_lending_product_list(self, **params):
        """
        Get Lending Product List
        """
        return self.binance_call.get_lending_product_list(**params)

    def get_lending_daily_quota_left(self, **params):
        """
        Get Left Daily Purchase Quota of Flexible Product.
        """
        return self.binance_call.get_lending_daily_quota_left(**params)

    def purchase_lending_product(self, **params):
        """
        Purchase Flexible Product.
        """
        return self.binance_call.purchase_lending_product(**params)

    def get_lending_daily_redemption_quota(self, **params):
        """
        Get Left Daily Redemption Quota of Flexible Product.
        """
        return self.binance_call.get_lending_daily_redemption_quota(**params)

    def redeem_lending_product(self, **params):
        """
        Redeem Flexible Product
        """
        return self.binance_call.redeem_lending_product(**params)

    def get_lending_position(self, **params):
        """
        Get Flexible Product Position
        """
        return self.binance_call.get_lending_position(**params)

    def get_lending_account(self, **params):
        """
        Get Lending Account Details
        """
        return self.binance_call.get_lending_account(**params)

    def get_lending_purchase_history(self, **params):
        """
        Get Lending Purchase History
        """
        return self.binance_call.get_lending_purchase_history(**params)

    def get_lending_redemption_history(self, **params):
        """
        Get Lending Redemption History
        """
        return self.binance_call.get_lending_redemption_history(**params)

    def get_lending_interest_history(self, **params):
        """
        Get Lending Interest History
        """
        return self.binance_call.get_lending_interest_history(**params)