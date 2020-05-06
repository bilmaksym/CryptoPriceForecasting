from .client import Client


class BinanceAccountDataEndpoints:
    """
        Wrapper for Account Data Endpoints
    """

    def __init__(self, api_key=None, api_secret=None, requests_params=None, tld='com'):
        self.binance_call = Client(api_key, api_secret, requests_params, tld)

    def create_order(self, **params):
        """
        Send in a new order
        Any order with an icebergQty MUST have timeInForce set to GTC.

        :param symbol: required e.g BNBBTC
        :param side: required
        :param type: required
        :param timeInForce: required if limit order
        :param quantity: required
        :param quoteOrderQty: amount the user wants to spend (when buying) or receive (when selling)
                of the quote asset, applicable to MARKET orders
        :param price: required
        :param newClientOrderId: A unique id for the order. Automatically generated if not sent.
        :param icebergQty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        :param newOrderRespType: Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.create_order(**params)

    def order_limit(self, **params):
        """
        Send in a new limit order
        Any order with an icebergQty MUST have timeInForce set to GTC.

        :param symbol: required
        :param side: required
        :param quantity: required
        :param price: required
        :param timeInForce: default Good till cancelled
        :param newClientOrderId: A unique id for the order. Automatically generated if not sent.
        :param icebergQty: Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        :param newOrderRespType: Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.order_limit(**params)

    def order_limit_buy(self, **params):
        """
        Send in a new limit buy order
        Any order with an icebergQty MUST have timeInForce set to GTC.

        :param symbol: required
        :param quantity: required
        :param price: required
        :param timeInForce: default Good till cancelled
        :param newClientOrderId: A unique id for the order. Automatically generated if not sent.
        :param stopPrice: Used with stop orders
        :param icebergQty: Used with iceberg orders
        :param newOrderRespType: Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.order_limit_buy(**params)

    def order_limit_sell(self, **params):
        return self.binance_call.order_limit_sell(**params)

    def order_market(self, **params):
        """
        Send in a new limit sell order

        :param symbol: required
        :param quantity: required
        :param price: required
        :param timeInForce: default Good till cancelled
        :param newClientOrderId: A unique id for the order. Automatically generated if not sent.
        :param stopPrice: Used with stop orders
        :param icebergQty: Used with iceberg orders
        :param newOrderRespType: Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
        :param recvWindow: the number of milliseconds the request is valid for

            :returns: API response
        """
        return self.binance_call.order_market(**params)

    def order_market_buy(self, **params):
        """
        Send in a new market buy order

        :param symbol: required
        :param quantity: required
        :param quoteOrderQty: the amount the user wants to spend of the quote asset
        :param newClientOrderId: A unique id for the order. Automatically generated if not sent.
        :param newOrderRespType: Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.order_market_buy(**params)

    def order_market_sell(self, **params):
        """
        Send in a new market sell order

        :param symbol: required
        :param quantity: required
        :param quoteOrderQty: the amount the user wants to receive of the quote asset
        :param newClientOrderId: A unique id for the order. Automatically generated if not sent.
        :param newOrderRespType: Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.order_market_sell(**params)

    def create_oco_order(self, **params):
        """
        Send in a new OCO order

        :param symbol: required
        :param listClientOrderId: A unique id for the list order. Automatically generated if not sent.
        :param side: required
        :param quantity: required
        :param limitClientOrderId: A unique id for the limit order. Automatically generated if not sent.
        :param price: required
        :param limitIcebergQty: Used to make the LIMIT_MAKER leg an iceberg order.
        :param stopClientOrderId: A unique id for the stop order. Automatically generated if not sent.
        :param stopPrice: required
        :param stopLimitPrice: If provided, stopLimitTimeInForce is required.
        :param stopIcebergQty: Used with STOP_LOSS_LIMIT leg to make an iceberg order.
        :param stopLimitTimeInForce: Valid values are GTC/FOK/IOC.
        :param newOrderRespType: Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.create_oco_order(**params)

    def order_oco_buy(self, **params):
        """
        Send in a new OCO buy order

        :param symbol: required
        :param listClientOrderId: A unique id for the list order. Automatically generated if not sent.
        :param quantity: required
        :param limitClientOrderId: A unique id for the limit order. Automatically generated if not sent.
        :param price: required
        :param limitIcebergQty: Used to make the LIMIT_MAKER leg an iceberg order.
        :param stopClientOrderId: A unique id for the stop order. Automatically generated if not sent.
        :param stopPrice: required
        :param stopLimitPrice: If provided, stopLimitTimeInForce is required.
        :param stopIcebergQty: Used with STOP_LOSS_LIMIT leg to make an iceberg order.
        :param stopLimitTimeInForce: Valid values are GTC/FOK/IOC.
        :param newOrderRespType: Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """

        return self.binance_call.order_oco_buy(**params)

    def order_oco_sell(self, **params):
        """
         Send in a new OCO sell order

        :param symbol: required
        :param listClientOrderId: A unique id for the list order. Automatically generated if not sent.
        :param quantity: required
        :param limitClientOrderId: A unique id for the limit order. Automatically generated if not sent.
        :param price: required
        :param limitIcebergQty: Used to make the LIMIT_MAKER leg an iceberg order.
        :param stopClientOrderId: A unique id for the stop order. Automatically generated if not sent.
        :param stopPrice: required
        :param stopLimitPrice: If provided, stopLimitTimeInForce is required.
        :param stopIcebergQty: Used with STOP_LOSS_LIMIT leg to make an iceberg order.
        :param stopLimitTimeInForce: Valid values are GTC/FOK/IOC.
        :param newOrderRespType: Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.order_oco_sell(**params)

    def create_test_order(self, **params):
        """
        Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it into the matching engine.

        :param symbol: required
        :param side: required
        :param type: required
        :param timeInForce: required if limit order
        :param quantity: required
        :param price: required
        :param newClientOrderId: A unique id for the order. Automatically generated if not sent.
        :param icebergQty: Used with iceberg orders
        :param newOrderRespType: Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
        :param recvWindow: The number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.create_test_order(**params)

    def get_order(self, **params):
        """
            Check an order's status. Either orderId or origClientOrderId must be sent.

            :param symbol: required
            :param orderId: The unique order id
            :param origClientOrderId: optional
            :param recvWindow: the number of milliseconds the request is valid for

            :returns: API response
        """
        return self.binance_call.get_order(**params)

    def get_all_orders(self, **params):
        """
        Get all account orders; active, canceled, or filled.

                :param symbol: required
                :type symbol: str
                :param orderId: The unique order id
                :type orderId: int
                :param limit: Default 500; max 500.
                :type limit: int
                :param recvWindow: the number of milliseconds the request is valid for
                :type recvWindow: int

                :returns: API response
        """
        return self.binance_call.get_all_orders(**params)

    def cancel_order(self, **params):
        """
        Cancel an active order. Either orderId or origClientOrderId must be sent.

        :param symbol: required
        :param orderId: The unique order id
        :param origClientOrderId: optional
        :param newClientOrderId: Used to uniquely identify this cancel. Automatically generated by default.
        :param recvWindow: the number of milliseconds the request is valid for

        :returns: API response
        """
        return self.binance_call.cancel_order(**params)

    def get_open_orders(self, **params):
        """
        Get all open orders on a symbol.

        :param symbol: optional
        :type symbol: str
        :param recvWindow: the number of milliseconds the request is valid for
        :type recvWindow: int

        :returns: API response
        """
        return self.binance_call.get_open_orders(**params)
