import yfinance as yf
import pandas as pd
import os

tickers = ["SPY", "^VIX", "XLK", "XLF", "XLV", "XLE"]

df = yf.download(tickers, start="2010-01-01", end="2026-01-01", group_by='ticker')

df_close = pd.DataFrame({
    'SPY': df['SPY']['Close'],
    'VIX': df['^VIX']['Close'],
    'XLK': df['XLK']['Close'],
    'XLF': df['XLF']['Close'],
    'XLV': df['XLV']['Close'],
    'XLE': df['XLE']['Close']
})
df_close = df_close.ffill().dropna()

save_directory = "data/raw"
file_path = f"{save_directory}/SP500_Market_Data.csv"

os.makedirs(save_directory, exist_ok = True)

df_close.to_csv(file_path)
