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
    print(response.text)
    if response.status_code == 200:
        # print(response.text.splitlines()[1:])
        data = pd.read_csv(response.text.splitlines())
        # data = pd.read_csv(response.text.splitlines()[1:])
        # data['ticker'] = ticker
        return response.text
    else:
        return None


# Fetch data for all tickers and concatenate into a single DataFrame
# data = pd.concat([get_historical_data(ticker) for ticker in tickers])
[get_historical_data(ticker) for ticker in tickers]

# Rename columns and convert date to datetime
# data.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'ticker']
# data['date'] = pd.to_datetime(data['date'])

# Sort data by date and ticker
# data = data.sort_values(['ticker', 'date'])

# Print the resulting DataFrame
