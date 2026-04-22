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

