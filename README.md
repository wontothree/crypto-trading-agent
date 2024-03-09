# Auto-trading

- Coin(binance, upbit)
- Stock

## Function

- 관찰하는 함수
- 매수하는 함수
- 매도하는 함수

## Monitoring System

모든 코인의 가격을 실시간으로 모니터링한다.

- 분봉, 일봉, 주봉, 월봉
- 거래량

## Reporting System

매수, 매도 결정 시 디스코드 봇(JARVIS)가 PUSH 알림을 보낸다.

## Review System

## Algorithm

알고리즘을 통해 다음 세 가지를 정할 수 있어야 한다. - 진입가, 익절가, 손절가

고려해야 할 사항

추세선, 이동평균선, 거래량, 캔들

절대 몰빵하면 안 되고, 소액으로 여러 번

안전성을 최우선으로 고려하자.

전체적인 장에 대한 고려를 할 수 있어야 한다.

특정 시점의 데이터를 가져올 수 있을까?

Index : SQZMOM_LB

### Algorithm 1

지정가에서 구매한다. 그 가격을 저장한다.

특정 가격에서 판매한다.

## 투자 기법

|투자 기법|보유기간|
|---|---|
|스캘핑|3분 이내|
|데이트트레이딩|하루|
|스윙 매매|하루 이상 일주일 이내|

## Dependency

[ccxt](https://github.com/ccxt/ccxt) : A Javascript / Python / PHP library for cryptocurrency trading and e-commerce with support for many bitcoin/ether/altcoin exchange markets and merchant APIs.

```
pip install ccxt 
```
