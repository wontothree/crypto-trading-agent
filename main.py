from classes import Myupbit

# 시장가 주문
# upbit.create_market_order("TRX/KRW", "buy", 10000, 1) # 10,000 x 1 원 어치
# upbit.create_market_order("TRX/KRW", "sell", ) # 주문수량

# 지정가 주문
# upbit.create_limit_order("TRX/KRW", "buy", 40, 152) # 수량 - 금액
# upbit.create_limit_order("TRX/KRW", "sell", , ) # 수량 - 금액


access_key = "TQcHNv10q7AG2FxSkEhadyQNmf7JEvVmhmoTqQzV"
secret_key = "Pywp6HfRHcXqoRGcJRQZKF9C2FTGBekCZWQpKk0R"

sewon_upbit = Myupbit(access_key, secret_key)

while True:
    sewon_upbit.watch_and_order("TRX/KRW", 10000, 0)
    sewon_upbit.watch_and_order("BTC/KRW", 10000, 0)
    sewon_upbit.watch_and_order("XRP/KRW", 10000, 0)



# try :
#     upbit.create_market_order("ABC/KRW", "buy", 10000, 1) # error code
# except Exception as e:
#     print("error arise")
#     print(e)