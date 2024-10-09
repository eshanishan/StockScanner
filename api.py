import requests
from datetime import date, timedelta
from api_keys import apikeys

api_key = apikeys['key1']
#api_key = apikeys['key2']

def get_overview_data(symbol):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data
def get_sentiment_data(symbol):
    dashed_year = date.today() - timedelta(days=365)
    year_before = str(dashed_year).replace("-", "")
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&time_from={year_before}T0000&ticker={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# earnings per share but if they are in the same industry and same stage
# make it a small group of of things like eps and p/e ratio and other things so 
# you can weight them and then compare them to the other company