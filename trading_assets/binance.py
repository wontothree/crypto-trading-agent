import ccxt
import pprint
import pandas as pd


binance = ccxt.binance()
markets = binance.load_markets()
# print(markets)

btc = binance.fetch_ticker("BTC/USDT")
# pprint.pprint(btc['last'])

# 일봉
btc_ohlcv = binance.fetch_ohlcv("BTC/USDT", timeframe='1d')

df = pd.DataFrame(btc_ohlcv, columns=[
                  'datatime', 'open', 'high', 'low', 'close', 'volume'])
df['datatime'] = pd.to_datetime(df['datatime'], unit='ms')
df.set_index('datatime', inplace=True)

print(df.loc["2024-02"])
