import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
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

def plot_dashboard(df,ticker,short,long):
    fig = plt.figure(figsize=(14,10))
    fig.suptitle(f"{ticker} - Stock Dashboard", fontsize = 16 , fontweight = "bold",y =0.98)
    gs = gridspec.GridSpec(3,1,figure = fig ,hspace = 0.45)

    ax1 = fig.add_subplot(gs[0])
    ax1.plot(df.index,df["Close"], label = "Close Price", color = "#1f77b4", linewidth=1.5)
    ax1.plot(df.index,df["MA20"] , label = "20-Day MA", color = "#ff7f0e" , linewidth = 1.2 , linestyle = "--")
    ax1.plot(df.index, df["MA50"], label="50-Day MA", color="#2ca02c", linewidth=1.2, linestyle="--")
    ax1.set_title("Closing Price with Moving Averages")
    ax1.set_ylabel("Price (USD)")
    ax1.legend(loc = "upper left",fontsize = 8)
    ax1.grid(True,alpha = 0.3)

    ax2 = fig.add_subplot(gs[1])
    ax2.bar(df.index,df["Volume"].squeeze(), color="#aec7e8", width=0.8, label="Volume")
    ax2.set_title("Daily Trading Volume")
    ax2.set_ylabel("Volume")
    ax2.grid(True,alpha = 0.3, axis = "y")

    ax3 = fig.add_subplot(gs[2])
    returns = df["Daily Return (%)"].dropna()
    ax3.hist(returns,bins = 40 , color = "#ffbb78",edgecolor="white", linewidth=0.5 )
    ax3.axvline(returns.mean(),color = "red" , linestyle = "--" ,linewidth=1.2,label=f"Mean: {returns.mean():.2f}%")
    ax3.axvline(0,color = "black",linestyle="-",linewidth = 0.8,alpha = 0.5)
    ax3.set_title("Distribution of Daily Returns")
    ax3.set_xlabel("Daily Return (%)")
    ax3.set_ylabel("Frequency")
    ax3.legend(fontsize = 8)
    ax3.grid(True , alpha = 0.3,axis="y")

    plt.savefig("stock_dashboard.png", dpi=150, bbox_inches="tight")
    print("Chart saved → stock_dashboard.png")
    plt.show()  

def main():
    print(f"Fetching {PERIOD} of data for {TICKER} ...")   
    df = fetch_data(TICKER,PERIOD)
    df = add_moving_averages(df,MA_SHORT,MA_LONG)
    df = add_daily_returns(df)
    print_summary(df,TICKER)
    plot_dashboard(df, TICKER, MA_SHORT, MA_LONG)

if __name__ == "__main__":
    main()






