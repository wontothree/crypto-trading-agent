import ccxt

class Myupbit():
    # 생성자
    def __init__(self, access, secret):
        print("딱 한 번만 실행된다.")
        self.upbit = ccxt.upbit()
        self.upbit.apiKey = access
        self.upbit.secret = secret
        self.is_buy = False

    def watch_and_order(self, symbol, money, watch_percent):
        print("가격을 감시하다가 매수를 하는 함수")
        infos = self.upbit.fetch_ticker(symbol)
        # print(infos)
        price = infos["close"]
        percent = infos["percentage"] * 100
        rounded_percent = round(percent, 2)
        print(f"현재 {symbol}의 가격은 {price}원이고 전일대비 {rounded_percent}% 입니다!")

        if percent < watch_percent and not self.is_buy:
            self.upbit.create_market_order(symbol, "buy", money, 1)
            self.is_buy = True

