import ccxt
import pprint


binance = ccxt.binance()
markets = binance.load_markets()

btc = binance.fetch_ticker("BTC/USDT")
pprint.pprint(btc['last'])

