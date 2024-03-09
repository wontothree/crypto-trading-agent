import ccxt
from datetime import datetime

import yaml


with open('config.yaml', encoding='UTF-8') as f:
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
