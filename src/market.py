import datetime
import os
from dotenv import load_dotenv
load_dotenv()

class Market:
    def __init__(self, api_client):
        self.api_client = api_client
    def get_price(self, ticker):
        endpoint = "/query"
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": ticker,
            "apikey": os.getenv("ALPHA_VANTAGE_API_KEY")
        }
        metadata = self.api_client.get(endpoint, params=params)
        latest_date = datetime.date.today()
        while latest_date.strftime("%Y-%m-%d") not in metadata["Time Series (Daily)"].keys():
             latest_date -= datetime.timedelta(days=1)
        return float(metadata["Time Series (Daily)"][latest_date.strftime("%Y-%m-%d")]["4. close"])