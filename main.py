from trading_assets.upbit import Upbit


sewon_upbit = Upbit()

# 시장가 주문
# upbit.create_market_order("TRX/KRW", "buy", 10000, 1) # 10,000 x 1 원 어치
# upbit.create_market_order("TRX/KRW", "sell", ) # 주문수량

# 지정가 주문
# upbit.create_limit_order("TRX/KRW", "buy", 40, 152) # 수량 - 금액
# upbit.create_limit_order("TRX/KRW", "sell", , ) # 수량 - 금액

while True:
    # sewon_upbit.watch_and_order("BTC/KRW", 100000, 0)
    sewon_upbit.observe("BTC/KRW")


# try :
#     upbit.create_market_order("ABC/KRW", "buy", 10000, 1) # error code
# except Exception as e:
#     print("error arise")
#     print(e)
