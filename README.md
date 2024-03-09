# Auto-trading

- Coin (Binance, Upbit)
- Stock

## Dependency

[ccxt](https://github.com/ccxt/ccxt) : A Javascript / Python / PHP library for cryptocurrency trading and e-commerce with support for many bitcoin/ether/altcoin exchange markets and merchant APIs.

```
pip install ccxt 
```

## Trading System

- BTC, 10만원, Leverage x 11, 5분봉
- 진입가 : protected highs & lows 파란색 삼각형이 나온다. 그리고 2분 동안 유지된다.
    - 익절가 = 진입가의 18%, 손절가 = 진입가의 13%
- [조건] 10일 이동평균선이 15일 이동평균선과 20일 이동평균선을 상향돌파한다.
    - 익절가 = 25%
    - [조건] 10일 이동평균선이 15일 이동평균선과 20일 이동평균선을 하향 돌파한다.
        - 손절가 = 현재가

## Reporting System

매수, 매도 결정 시 디스코드 봇이 PUSH 알림을 보낸다.

## Review System
