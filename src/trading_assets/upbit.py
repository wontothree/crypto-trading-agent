import ccxt
from datetime import datetime

import yaml
import pprint

with open('../../config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)

UPBIT_ACCESS_KEY = _cfg["UPBIT_ACCESS_KEY"]
UPBIT_SECRET_KEY = _cfg["UPBIT_SECRET_KEY"]

class Upbit():
    def __init__(self):
        """
        Parameters
        ----------
        is_buy : 포지션을 결정하는 스위칭 역할 변수
        """
        self.upbit = ccxt.upbit()
        self.upbit.apiKey = UPBIT_ACCESS_KEY
        self.upbit.secret = UPBIT_SECRET_KEY
        self.is_buy = False

    def observe(self, symbol):
        """
        가격을 감시하는 함수

        Parameters
        ----------
        symbol : coin symbol.
            ex) BTC/KRW, DOGE/KRW, TRX/KRW, XRP/KRW.
        """

        infos = self.upbit.fetch_ticker(symbol)
        price = infos["close"]
        formatted_price = "{:,}".format(price)

        percent = infos["percentage"] * 100  # 백분율
        rounded_percent = round(percent, 3)  # 소수점 두 자리에서 반올림
        formatted_percent = f"{rounded_percent:.3f}"

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        print(
            f"| {formatted_time} | {symbol} | 현재가(원) : {formatted_price} | 전일 대비 상승률(%) : {formatted_percent} |")

    def watch_and_order(self, symbol, money, watch_percent):
        """
        가격을 감시하다가 매수를 하는 함수

        Parameters
        ----------
        symbol : coin.
            ex) BTC/KRW, DOGE/KRW, TRX/KRW, XRP/KRW.
        money : 매수 금액.
        watch_percent : 구매하길 바라는 퍼센트 하락.
        """

        infos = self.upbit.fetch_ticker(symbol)
        price = infos["close"]
        percent = infos["percentage"] * 100  # 백분율
        rounded_percent = round(percent, 3)  # 소수점 두 자리에서 반올림

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"{formatted_time } | {symbol}의 가격은 {price}원이고, 전일대비 {rounded_percent}%입니다!")

        if percent < watch_percent and not self.is_buy:
            self.upbit.create_market_order(symbol, "buy", money, 1)
            self.is_buy = True

    # --------------------------------------------------

    def print_full_ticker_info(self, symbol):
        """
        해당 심볼의 ticker 전체 정보를 출력합니다.
        """
        ticker = self.upbit.fetch_ticker(symbol)
        print(f"=== Ticker Info for {symbol} ===")
        pprint.pprint(ticker)

        print("\n=== Raw info from exchange ===")
        pprint.pprint(ticker.get('info', {}))

    def print_volume_info(self, symbol):
        """
        심볼을 받아 해당 심볼의 ticker 정보를 fetch하고
        거래량 관련 정보만 예쁘게 출력합니다.

        Parameters
        ----------
        symbol : str
            조회할 심볼 (예: 'BTC/KRW')
        """
        ticker = self.upbit.fetch_ticker(symbol)

        base_volume = ticker.get('baseVolume', None)
        quote_volume = ticker.get('quoteVolume', None)

        info = ticker.get('info', {})
        acc_trade_volume = info.get('acc_trade_volume', None)
        acc_trade_volume_24h = info.get('acc_trade_volume_24h', None)
        acc_trade_price = info.get('acc_trade_price', None)
        acc_trade_price_24h = info.get('acc_trade_price_24h', None)
        trade_volume = info.get('trade_volume', None)

        print("="*40)
        print(f"{symbol} 거래량 정보 (기준 통화 단위 / 가격 단위)")
        print("- 기준 통화 거래량 (baseVolume):", f"{float(base_volume):,.8f}" if base_volume else "N/A")
        print("- 가격 단위 거래량 (quoteVolume):", f"{float(quote_volume):,.8f}" if quote_volume else "N/A")
        print("- 누적 거래량 (acc_trade_volume):", f"{float(acc_trade_volume):,.8f}" if acc_trade_volume else "N/A")
        print("- 24시간 누적 거래량 (acc_trade_volume_24h):", f"{float(acc_trade_volume_24h):,.8f}" if acc_trade_volume_24h else "N/A")
        print("- 누적 거래대금 (acc_trade_price):", f"{float(acc_trade_price):,.8f}" if acc_trade_price else "N/A")
        print("- 24시간 누적 거래대금 (acc_trade_price_24h):", f"{float(acc_trade_price_24h):,.8f}" if acc_trade_price_24h else "N/A")
        print("- 최근 체결 거래량 (trade_volume):", trade_volume if trade_volume else "N/A")
        print("="*40)

# only for test
if __name__ == "__main__":
    upbit = Upbit()
    # while True:
    #     upbit.print_full_ticker_info("BTC/KRW")
    # upbit.print_full_ticker_info("BTC/KRW")
    # upbit.print_volume_info("BTC/KRW")

    # ----------

    # while True:
    #     trades = upbit.upbit.fetch_trades("BTC/KRW", limit=500) # max: 500

    #     # for t in trades:
    #     #     print(t)

    #     # print(f"받아온 최근 체결 개수: {len(trades)}")

    #     buy_count = 0
    #     sell_count = 0

    #     for t in trades:
    #         side = t.get('side', None)
    #         if side == 'buy':
    #             buy_count += 1
    #         elif side == 'sell':
    #             sell_count += 1
    #         # print(t)

    #     print(f"받아온 최근 체결 개수: {len(trades)}")
    #     print(f"매수 체결 개수: {buy_count}")
    #     print(f"매도 체결 개수: {sell_count}")
            
    import time
    from datetime import datetime

    last_seen_timestamp = 0

    while True:
        trades = upbit.upbit.fetch_trades("BTC/KRW", limit=500)

        latest_trade = trades[0]
        latest_timestamp = latest_trade['timestamp']

        if latest_timestamp != last_seen_timestamp:
            last_seen_timestamp = latest_timestamp

            buy_count = sell_count = 0
            buy_volume = sell_volume = 0.0
            buy_total_krw = sell_total_krw = 0.0

            for t in trades:
                side = t.get('side')
                volume = float(t.get('amount') or t.get('volume') or 0)
                price = float(t.get('price') or 0)
                total = volume * price  # 체결 금액 (원화)

                if side == 'buy':
                    buy_count += 1
                    buy_volume += volume
                    buy_total_krw += total
                elif side == 'sell':
                    sell_count += 1
                    sell_volume += volume
                    sell_total_krw += total

            # 현재 시각 및 체결 시각
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            trade_time_str = datetime.fromtimestamp(latest_timestamp / 1000).strftime("%Y-%m-%d %H:%M:%S")

            # 현재 BTC 가격
            ticker = upbit.upbit.fetch_ticker("BTC/KRW")
            current_price = ticker['last']

            print(f"\n[현재 시각: {now_str}]")
            print(f"새로운 체결 발생 시각: {latest_timestamp} ({trade_time_str})")
            print(f"현재 BTC 가격: {current_price:,.0f} 원")
            print(f"총 트레이드 수: {len(trades)}")
            print(f"✅ 매수 — 횟수: {buy_count}, 총량: {buy_volume:.6f} BTC, 총액: {buy_total_krw:,.0f} 원")
            print(f"❌ 매도 — 횟수: {sell_count}, 총량: {sell_volume:.6f} BTC, 총액: {sell_total_krw:,.0f} 원")

        time.sleep(0.1)
