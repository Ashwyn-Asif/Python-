import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

TICKER = "AAPL"
PERIOD = "6mo"
MA_SHORT = 20
MA_LONG = 50
def fetch_data(ticker,period):
    df = yf.download(ticker,period = period,auto_adjust=True,progress = False)
    return df
def add_moving_averages(df,short,long):
    df["MA20"] = df["Close"].rolling(window=short).mean()
    df["MA50"] = df["Close"].rolling(window=long).mean()
    return df
def add_daily_returns(df):
    df["Daily Return (%)"] = df["Close"].pct_change()*100
    return df

df = fetch_data(TICKER,PERIOD)
df = add_moving_averages(df,MA_SHORT,MA_LONG)
df = add_daily_returns(df)
print(df[["Close","Daily Return (%)"]].tail(10))








