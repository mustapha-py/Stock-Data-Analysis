# Importing necessary libraries
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime as dt
import getFamaFrenchFactors as gff
import statsmodels.api as sm
import seaborn as sns

# Override Yahoo Finance's pandas datareader
yf.pdr_override()

# Set the time range for stock data
start = dt(2014, 1, 1)
end = dt(2024, 1, 3)

# List of tech stocks
tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

# Download stock data for each tech company
for stock in tech_list:
    globals()[stock] = yf.download(stock, start, end)  # Download and store in a DataFrame

# Store DataFrames and company names in lists for easier access
company_list = [AAPL, GOOG, MSFT, AMZN]
company_name = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]


# ## 1. Calculate Daily Returns
for stock in tech_list:
    df = globals()[stock]
    df['Daily Return'] = (df['Adj Close'] / df['Adj Close'].shift(1)) - 1

# Example: Display AMZN's DataFrame with daily returns
AMZN


# ## 2. Calculate Monthly and Yearly Returns
for stock in tech_list:
    df = globals()[stock]
    df = df.asfreq('D')  # Ensure daily frequency
    df['Adj Close'] = df['Adj Close'].ffill()  # Forward-fill missing data

    # Calculate monthly and yearly returns
    df['Monthly Return'] = df['Adj Close'].resample('M').ffill().pct_change()
    df['Yearly Return'] = df['Adj Close'].resample('Y').ffill().pct_change()

    globals()[stock] = df  # Update the DataFrame in globals()

# Example: Display AMZN's yearly return
AMZN['Yearly Return']


# ## 3. Calculate Cumulative Returns
def calculate_cumulative_return(df):
    df['Cumulative Return'] = (df['Adj Close'] / df['Adj Close'].iloc[0]) - 1
    return df

for stock in tech_list:
    df = globals()[stock]
    df = calculate_cumulative_return(df)
    globals()[stock] = df  # Update global variable

# Example: Display AMZN info
AMZN.info()


# ## 4. Save Stock Data to CSV
# Uncomment if needed
# AAPL.to_csv(r'......\AAPL.csv')
# GOOG.to_csv(r'......\GOOG.csv')
# MSFT.to_csv(r'......\MSFT.csv')
# AMZN.to_csv(r'......\AMZN.csv')


# ## 5. Stocks vs Market: Monthly Returns
monthly_returns_dict = {}

for stock in tech_list:
    df = globals()[stock]
    monthly_returns_dict[stock] = df['Monthly Return']

# Combine monthly returns into a single DataFrame
Monthly_Returns = pd.concat(monthly_returns_dict, axis=1)
Monthly_Returns.columns = [f'{stock}' for stock in tech_list]

# Remove missing data
Monthly_Returns = Monthly_Returns.dropna()
Monthly_Returns.head()


# ## 6. Fama-French Market Data
ff3_Monthly = pd.DataFrame(gff.famaFrench3Factor(frequency='m'))
ff3_Monthly.rename(columns={'date_ff_factors': 'Date'}, inplace=True)
ff3_Monthly.set_index('Date', inplace=True)
ff3_Monthly.head()


# ## 7. Merging Stock and Market Data
Stocks_Market = ff3_Monthly.merge(Monthly_Returns, on='Date')

# Keep the last 60 observations
Stocks_Market = Stocks_Market.tail(60)
Stocks_Market.head()


# ## 8. Calculate Excess Returns (Stock - Risk-Free Rate)
for stock in tech_list:
    Stocks_Market[f'{stock}-RF'] = Stocks_Market[stock] - Stocks_Market['RF']

Stocks_Market.head()


# ## 9. Calculate Market Returns
Stocks_Market['Mkt'] = Stocks_Market['Mkt-RF'] + Stocks_Market['RF']
Stocks_Market.head(10)


# ## 10. Save Merged Data to CSV 
# Uncomment if needed
# Stocks_Market.to_csv(r'......\Stocks_Market.csv')


# ## 11. CAPM Calculations

# 11.1 Calculate market variance (Annualized)
market_var = Stocks_Market['Mkt'].var() * 12
print("Market Variance:", market_var)

# 11.2 Calculate covariance matrix (Annualized)
cov = Stocks_Market.cov() * 12
print("Covariance Matrix:\n", cov)

# 11.3 Covariance of AAPL with the market
AAPL_cov_with_market = cov.loc['AAPL-RF', 'Mkt-RF']
print("AAPL Covariance with Market:", AAPL_cov_with_market)


# 11.4 Calculate Sharpe Ratio for AMZN (Annualized)
AMZN_sharpe = (Stocks_Market['AMZN-RF'].mean() / Stocks_Market['AMZN'].std()) * np.sqrt(12)
print("AMZN Sharpe Ratio:", AMZN_sharpe)


# ## 12. Regression (CAPM) for GOOG

# Prepare data for regression
x = Stocks_Market['Mkt-RF']
y = Stocks_Market['GOOG-RF']
X1 = sm.add_constant(x)  # Add constant for the intercept

# Run OLS regression
model = sm.OLS(y, X1)
results = model.fit()

# Display regression summary
print(results.summary())

# Extract intercept and beta
intercept, beta = results.params
print("Beta for GOOG:", beta)


# ## 13. Expected Return Calculation (CAPM)

# Risk-free rate and market premium
risk_free = Stocks_Market['RF'].mean()
market_premium = Stocks_Market['Mkt-RF'].mean()

# Calculate expected return for AAPL (CAPM formula)
AAPL_Expected_return = risk_free + beta * market_premium
print("AAPL Expected Return:", AAPL_Expected_return)

# Annualized expected return
Yearly_Expected_return = AAPL_Expected_return * 12
print("AAPL Yearly Expected Return:", Yearly_Expected_return)
