import ccxt
import yaml
import pprint
import pandas as pd


with open('../config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
BINACE_APT_KEY = _cfg["BINACE_APT_KEY"]
BINACE_SECRET_KEY = _cfg["BINACE_SECRET_KEY"]


binance = ccxt.binance(
    config={"apiKey": BINACE_APT_KEY, "secret": BINACE_SECRET_KEY})

# markets = binance.load_markets()
# # print(markets)

# btc = binance.fetch_ticker("BTC/USDT")
# # pprint.pprint(btc['last'])

# # 일봉
# btc_ohlcv = binance.fetch_ohlcv("BTC/USDT", timeframe='1d')

# df = pd.DataFrame(btc_ohlcv, columns=[
#                   'datatime', 'open', 'high', 'low', 'close', 'volume'])
# df['datatime'] = pd.to_datetime(df['datatime'], unit='ms')
# df.set_index('datatime', inplace=True)

# # print(df.loc["2024-02"])


# # 잔액
# balance = binance.fetch_balance()  # 현물
# balance = binance.fetch_balance(params={'type': "future"})  # 선물
# # print(balance['USDT'])


# 현물 거래(지정가 매수)
order = binance.create_limit_buy_order(
    symbol="XRP/USDT",
    amount=0.6,
    price=7
)

pprint.pprint(order)
