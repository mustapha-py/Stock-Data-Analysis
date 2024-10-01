# Tech Giants: Stock Data Analysis (2014-2023)
This repository contains an interactive stock data analysis dashboard for America's leading tech companies: Apple (AAPL), Amazon (AMZN), Google (GOOG), and Microsoft (MSFT). The dashboard has been created using Power BI and data retrieved via the Yahoo Finance API in Python.

## Table of Contents
- [Overview](#overview)
- [Data Source](#data-source)
- [Project Structure](#project-Structure)
- [Features](#features)
- [Visualization](#visualization)
- [How to Use](#how-to-Use)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project provides a comprehensive analysis of stock performance, financial metrics, and risk analysis of four major tech companies between 2014 and 2023. The goal is to offer insights into price movements, returns, and risk measures like CAPM and - Sharpe Ratio using interactive visuals.

## Data Source
Data is sourced from the Yahoo Finance API using the yfinance library in Python.
The data spans from January 2014 to December 2023 and includes:
- Stock Prices: Open, Close, High, Low
- Volume
- Returns and Excess Returns
- Financial Metrics: Market Cap, P/E Ratio, Profit Margins, Dividend Yield, etc.

Python scripts used to retrieve and preprocess the data are located in the /scripts folder.

## Project Structure
```bash
├── README.md
├── scripts
│   └── data_preparation.py       # Python script to fetch and prepare stock data from Yahoo Finance
├── data
│   └── *.csv                  # Cleaned stock data
├── Tech Giants Stock Data Analysis.pbix   # Power BI report file
├── images
│   └── dashboard_screenshot_1.jpg # Example screenshots of the Power BI dashboard
└── requirements.txt           # Python dependencies
```

## Features
### Stock Analysis:
- Historical prices (Open, Close, High, Low)
- Price trends over time
- Volume analysis

### Financial Metrics:
- Market capitalization
- Dividend rates and payout ratios
- P/E ratios (trailing and forward)

### Risk Analysis:
- CAPM (Beta, Alpha)
- Sharpe Ratio
- Cumulative returns

## Visualization
The Power BI report contains multiple pages, including:
- Home Page: Overview of the companies analyzed.
- Key Statistics: Financial metrics like P/E ratio, market cap, profit margins.
- Candlestick Chart: Visual representation of stock price movements.
- Returns: Daily, monthly, and yearly returns across time.
- CAPM: Expected returns based on the Capital Asset Pricing Model (CAPM).
Screenshots of the visuals can be found in the /images folder.

## How to Use
- Access the Power BI report (Tech Giants: Stock Data Analysis (2014-2023)) in Power BI Service.
  -- [Report LINK](https://tinyurl.com/4k3pnc9a)
  > Right-click the link and select "Open in new tab" or "Open in new window" for better navigation.
  
- Select a company from the sidebar to view its specific stock data and financial metrics.
- Use the slicers (Date, Company) to filter data for a specific period or company.
- Navigate between the different pages for in-depth analysis of stock performance and risk.




## Contributing
Feel free to contribute to this project by submitting a pull request. For major changes, please open an issue to discuss what you would like to change.

## License
This project is licensed under the MIT License.
