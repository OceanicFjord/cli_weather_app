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

    def get_forecast(self, city: str) -> List[Dict]:
        url = self.BASE_URL + "forecast"

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "de"
        }

        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        result = []
        seen_dates = set()
        
        for entry in data["list"]:
            dt_txt = entry["dt_txt"]
            date_part, time_part = dt_txt.split(" ")
            if time_part == "12:00:00" and date_part not in seen_dates:
                seen_dates.add(date_part)
                result.append({
                    "date": date_part,
                    "temp": entry["main"]["temp"],
                    "description": entry["weather"][0]["description"].capitalize(),
                })
                if len(result) >= 5:
                    break
        return result