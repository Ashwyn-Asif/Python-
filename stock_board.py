import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

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

def print_summary(df,ticker):
    returns = df["Daily Return (%)"].dropna()
    latest = df["Close"].iloc[-1].item()
    high = df["Close"].max().item()
    low = df["Close"].min().item()

    print(f"\n{'-'*40}")
    print(f" {ticker} - Summary Statistics")
    print(f"{'-'*40}")
    print(f" Latest close  : ${latest:.2f}")
    print(f" Period high   : ${high:.2f}")
    print(f" Period low    : ${low:.2f}")
    print(f" Avg daily ret : {returns.mean():.3f}%")
    print(f" Volatility    : {returns.std():.3f}%")
    print(f" Best Day      : {returns.max():.2f}%")
    print(f" Worst Day     : {returns.min():.2f}%")
    print(f"{'-'*40}\n")


df = fetch_data(TICKER,PERIOD)
df = add_moving_averages(df,MA_SHORT,MA_LONG)
df = add_daily_returns(df)
print_summary(df,TICKER)








