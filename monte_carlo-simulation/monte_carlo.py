import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

TICKER = "AAPL"
START_PRICE = 260.0
DRIFT = 0.0003
VOLATILITY = 0.013
DAYS = 30
SIMULATIONS = 1000
CONFIDENCE = 0.95
INVESTMENT = 10000.0

def simulate_price_paths(start_price,drift,volatility,days,simulations):
    price_paths = np.zeros((days,simulations))
    price_paths[0] = start_price
    
    for day in range (1,days):
        random_shocks = np.random.normal(0,1,simulations)
        price_paths[day] = price_paths[day-1]*(1+drift+volatility*random_shocks)
    
    return price_paths

def calculate_var(price_paths,start_price,confidence,investment):
    final_prices=price_paths[-1]
    returns = (final_prices - start_price)/start_price

    var_percent = 1-confidence
    var_return = np.percentile(returns,var_percent *100) 
    var_dollar = var_return * investment

    return returns , var_return , var_dollar

def plot_simulation(price_paths,returns, var_returns,ticker,confidence):
    fig = plt.figure(figsize=(14,10))
    fig.suptitle(f"{ticker} - Monte Carlo VaR Simulation",fontsize = 16,fontweight="bold",y=0.98)
    gs = gridspec.GridSpec(2,1,figure=fig,hspace=0.4)

    ax1 = fig.add_subplot(gs[0])
    ax1.plot(price_paths,color="steelblue",alpha=0.05,linewidth=0.5)
    ax1.plot(price_paths.mean(axis=1),color="red",linewidth=2,label="Mean path")
    ax1.set_title(f"{SIMULATIONS} Simulated Price Paths over {DAYS} Days")
    ax1.set_xlabel("Days")
    ax1.set_ylabel("Price (USD)")
    ax1.legend(loc='upper left', fontsize=8)
    ax1.grid(True,alpha=0.3)

    ax2 = fig.add_subplot(gs[1])
    ax2.hist(returns*100,bins=50,color='#aec7e8',edgecolor="white",linewidth=0.5)
    ax2.axvline(var_returns*100,color="red",linestyle="--",linewidth=2,label=f"Var ({confidence*100:.0f}%): {var_returns*100:.2f}%")
    ax2.set_title("Distribution of Simulated 30 Day Returns")
    ax2.set_xlabel("Return (%)")
    ax2.set_ylabel("Frequency")
    ax2.legend(fontsize=8)
    ax2.grid(True,alpha=0.3,axis="y")
    plt.savefig("monte_carlo-simulation/monte_carlo.png", dpi=150, bbox_inches="tight")
    plt.show()

def print_summary(ticker,start_price,days,simulations,confidence,var_return,var_dollar,investment):
    print(f"\n{'-'*45}")
    print(f" {ticker} - Monte Carlo VaR Summary")
    print(f"{'-'*45}")
    print(f" Start Price   : ${start_price:.2f}")
    print(f" Horizon       : {days} days")
    print(f" Simulations   : {simulations:,}")
    print(f" Confidence    : {confidence*100:.0f}%")
    print(f"{'-'*45}")
    print(f" VaR Return    : {var_return*100:.2f}%")
    print(f" VaR Dollar    : ${var_dollar:.2f}")
    print(f"Investment     : ${investment:,.2f}")
    print(f"{'-'*45}")
    print(f"Interpretation : There is a {confidence*100:.0f}% chance")
    print(f"You will not lose more than ${abs(var_dollar):.2f}")
    print(f"over the next {days} days on a ${investment:,.2f} investment")
    print(f"{'-'*45}")

def main():
     print(f"Running Monte Carlo simulation for {TICKER}...")
     price_paths = simulate_price_paths(START_PRICE,DRIFT,VOLATILITY,DAYS,SIMULATIONS)
     returns, var_return, var_dollar = calculate_var(price_paths, START_PRICE, CONFIDENCE, INVESTMENT)
     print_summary(TICKER, START_PRICE, DAYS, SIMULATIONS, CONFIDENCE, var_return,var_dollar, INVESTMENT)
     plot_simulation(price_paths, returns, var_return, TICKER, CONFIDENCE)

if __name__ == "__main__":
    main()