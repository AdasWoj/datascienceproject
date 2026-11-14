import yfinance as yf
import pandas as pd

tickers = ["SPY", "^VIX", "GC=F"]

df = yf.download(tickers, start="2010-01-01", end="2026-01-01", group_by='ticker')

df_close = pd.DataFrame({
    'SPY': df['SPY']['Close'],
    'VIX': df['^VIX']['Close'],
    'Gold': df['GC=F']['Close']
})
df_close = df_close.ffill().dropna()

print(df_close.tail())
df_close.to_csv("SP500_Market_Data.csv")
