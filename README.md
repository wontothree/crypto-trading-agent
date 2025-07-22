# Crypto Trading System

- Upbit
- Binance

# Dependency

[ccxt](https://github.com/ccxt/ccxt) : A Javascript / Python / PHP library for cryptocurrency trading and e-commerce with support for many bitcoin/ether/altcoin exchange markets and merchant APIs.

```txt
pip install ccxt

pip install discord.py

pip install pyyaml
```

# Getting Started

## yaml

Root 경로에 config.yaml 파일을 만들고 다음 항목을 입력한다.

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

## Execute main.py

main.py를 실행하면, 실시간 BTC의 가격을 확인할 수 있다.

```txt
| 2025-04-17 16:53:30 | BTC/KRW | 현재가(원) : 122,211,000.0 | 전일 대비 상승률(%) : 0.296 |
```

## Discore

system/report.py를 실행하면, Discord Bot이 활성화된다.

```txt
2025-04-17 16:54:28 INFO     discord.client logging in using static token
2025-04-17 16:54:30 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: 0000).
JARVIS on online
```

# To-do

- [ ] Visualizing System
- [ ] Reporting System: 매수, 매도 결정 시 디스코드 봇이 PUSH 알림을 보낸다.
- [ ] Review System
