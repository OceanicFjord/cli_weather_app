import requests
from datetime import datetime
from typing import Dict, List


class WeatherClient:
    BASE_URL = "https://api.openweathermap.org/data/2.5/"

    def __init__(self, api_key: str):

        if not api_key:
            raise ValueError("Ein gültiger API-Key wird benötigt.")
        self.api_key = api_key

    def get_current(self, city: str) -> Dict:
        URL = self.BASE_URL + "weather"
        
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "de"
        }

        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        result = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
        return result

