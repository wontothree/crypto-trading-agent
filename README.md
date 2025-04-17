# Crypto Trading Agent

- Coin (Binance, Upbit)
- Stock

## Getting Started

- root 경로에 config.yaml 파일을 만들고 다음 항목을 입력한다.

```txt
# UPBIT
UPBIT_ACCESS_KEY : ""
UPBIT_SECRET_KEY : ""


# BINANCE
BINACE_APT_KEY : ""
BINACE_SECRET_KEY : ""


# DISCORD
DISCORD_BOT_TOKEN : ""
```

- 의존성을 설치한다.
- main.py를 실행하면, 실시간 BTC의 가격을 확인할 수 있다.

```txt
| 2025-04-17 16:53:30 | BTC/KRW | 현재가(원) : 122,211,000.0 | 전일 대비 상승률(%) : 0.296 |
```

- system/report.py를 실행하면, Discord Bot이 활성화된다.

```txt
2025-04-17 16:54:28 INFO     discord.client logging in using static token
2025-04-17 16:54:30 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: 0000).
JARVIS on online
```

## Dependency

[ccxt](https://github.com/ccxt/ccxt) : A Javascript / Python / PHP library for cryptocurrency trading and e-commerce with support for many bitcoin/ether/altcoin exchange markets and merchant APIs.

```txt
pip install ccxt

pip install discord.py

/Applications/Python\ 3.11/Install\ Certificates.command
```

## Trading System

example

```py
if (5분봉 차트에서 protected highs & lows에서 파란색 삼각형이 나온다. and 그것이 2분동안 유지된다.)
    진입가 = BTC x 11의 10만원 어치 시장가
    익절가 = 진입가의 18%
    손절가 = 진입가의 13%
    if (5분봉 차트에서 10일 이동평균선이 15일 이동평균선과 20일 이동평균선을 상향 돌파한다.)
        익절가 = 진입가의 25%
        if (5분봉 차트에서 10일 이동평균선이 15일 이동평균선과 20일 이동평균선을 하향 돌파한다.)
            손절가 = 현재가
```

## To-do

- [ ] Visualizing System
- [ ] Reporting System: 매수, 매도 결정 시 디스코드 봇이 PUSH 알림을 보낸다.
- [ ] Review System
