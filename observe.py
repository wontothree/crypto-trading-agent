import ccxt
from datetime import datetime

class Observe():
    def __init__(self):
        self.upbit = ccxt.upbit()


    def observe(self, symbol):
        """
        가격을 감시하는 함수

        Parameters
        ----------
        symbol : coin.
            ex) BTC/KRW, DOGE/KRW, TRX/KRW, XRP/KRW.
        """

        infos = self.upbit.fetch_ticker(symbol)
        price = infos["close"]
        formatted_price = "{:,}".format(price)

        percent = infos["percentage"] * 100 # 백분율
        rounded_percent = round(percent, 3) # 소수점 두 자리에서 반올림
        formatted_percent = f"{rounded_percent:.3f}"

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        print(f"| {formatted_time} | {symbol} | 현재가(원) : {formatted_price} | 전일 대비 상승률(%) : {formatted_percent} |")


