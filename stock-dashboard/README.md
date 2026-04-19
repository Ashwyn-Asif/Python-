# Stock Market Dashboard

A Python dashboard that fetches real stock market data and visualises 
price trends, trading volume, and return distribution for any publicly 
traded stock.

Built with: Python, yfinance, pandas, matplotlib

## Dashboard Preview

![Stock Dashboard](/Python-/stock-dashboard/stock_dashboard.png)

## What it does

- Fetches real historical stock data for any ticker using yfinance
- Calculates 20-day and 50-day simple moving averages to identify trends
- Computes daily percentage returns across the entire period
- Visualises all three in a clean three panel dashboard
- Prints key statistics to the console including volatility and best/worst days

## Concepts covered

- Moving averages and trend analysis (Golden Cross / Death Cross)
- Daily return calculation and volatility measurement
- Return distribution and its importance in quantitative finance
- Data cleaning and adjustment for stock splits and dividends

## How to run

Install dependencies:
```bash
pip install yfinance pandas matplotlib
```

Run the dashboard:
```bash
python stock_board.py
```

To analyse a different stock, change the ticker at the top of the file:
```python
TICKER = "TSLA"  # or any valid stock symbol
```

## Possible extensions

- Add RSI (Relative Strength Index) as a fourth panel
- Support multiple tickers for side by side comparison
- Add Bollinger Bands to the price chart
- Export summary statistics to a CSV file