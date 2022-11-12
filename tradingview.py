from tradingview_ta import TA_Handler, Interval, Exchange

tesla = TA_Handler(
    symbol="TSLA",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY
)
print(tesla.get_analysis().summary)

btc = TA_Handler(
    symbol="BTCUSDT",
    screener="crypto",
    exchange="COINBASE",
    interval=Interval.INTERVAL_5_MINUTES
)

print(btc.get_analysis().summary)
