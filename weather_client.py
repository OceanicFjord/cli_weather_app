import requests
from datetime import datetime
from typing import Dict, List


class WeatherClient:
    BASE_URL = "https://api.openweathermap.org/data/2.5/"

    def __init__(self, api_key: str):

        if not api_key:
            raise ValueError("Ein gültiger API-Key wird benötigt.")
        self.api_key = api_key