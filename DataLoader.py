from BinanceAPI.Controller_API import Controller
from datetime import timedelta
from datetime import datetime
import pandas


class DataLoader:

    def __init__(self, API_KEY, API_SECRET):
        self.binance_client = Controller(API_KEY, API_SECRET).market_data_endpoints()

    def load_data(self, symbol, kline_size, period):
        """
        Loads market data fopr a given period
        :param symbol: pair (example:BTCUSDT)
        :param kline_size: size of candles (example: 1m, 1h, 1d, etc.)
        :param period: period of time for which we loading data
        :return: pandas dataframe with market information for a given period
        """
        start_point = 0
        if kline_size == "1m":
            start_point = datetime.now().replace(microsecond=0, second=0) - timedelta(minutes=period) - timedelta(
                hours=3)  # here 3 is a difference between our time and exchange
        elif kline_size == "1h":
            start_point = datetime.now().replace(microsecond=0, second=0, minute=0) - timedelta(
                hours=period + 3)  # here 3 is a difference between our time and exchange
        elif kline_size == "1d":
            start_point = datetime.now().replace(microsecond=0, second=0, minute=0, hour=0) - timedelta(days=period)
        start_point = start_point.strftime("%d %b %Y %H:%M:%S")
        end_point = pandas.to_datetime(self.binance_client.get_klines(symbol=symbol, interval=kline_size)[-1][0],
                                       unit='ms').strftime(
            "%d %b %Y %H:%M:%S")
        klines = self.binance_client.get_historical_klines(symbol, kline_size, start_point, end_point)
        data = pandas.DataFrame(klines,
                                columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                                         'quote_av',
                                         'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
        data['timestamp'] = pandas.to_datetime(data['timestamp'], unit='ms')
        data.drop(data.tail(1).index, inplace=True)
        return data
