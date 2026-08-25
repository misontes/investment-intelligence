import requests
import time
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
    def get(self, endpoint, params=None): 
        time.sleep(5)
        response = requests.get(self.base_url + endpoint, params=params)
        response.raise_for_status()
        return response.json()