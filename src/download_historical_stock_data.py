import requests
import pandas as pd

# Replace with your Alpha Vantage API key
API_KEY = 'gS_2hnZuuKvBu-D_GWd9'

# List of stocks and ETFs to fetch data for
tickers = ['AAPL', 'GOOGL', 'AMZN', 'SPY', 'QQQ']


# Function to fetch historical data for a single ticker
def get_historical_data(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={API_KEY}&datatype=csv'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


# Fetch data for all tickers and concatenate into a single DataFrame
[get_historical_data(ticker) for ticker in tickers]
