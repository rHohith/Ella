import json
from urllib.request import urlopen
from utils.tools import write_json


def get_all_tickers():
    """
    Fetch tickers from Poloniex API and save to JSON file
    """

    response = urlopen('https://poloniex.com/public?command=returnTicker')
    response_data = response.read()
    tickers = [k for k, _ in json.loads(response_data).items() if k[:3] == 'BTC']
    tickers.sort()
    write_json('poloniex/data/tickers.json', tickers)
    return tickers


def get_tickers():
    """
    Fetch tickers from Poloniex API and save to JSON file
    """

    tickers = [
        'BTC_BELA',
        'BTC_DASH',
        'BTC_DOGE',
        'BTC_ETH',
        'BTC_LBC',
        'BTC_MAID',
        'BTC_XEM',
        'BTC_XMR',
    ]
    tickers.sort()
    write_json('poloniex/data/tickers.json', tickers)
    return tickers
