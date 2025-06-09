import argparse
import sys

from config_manager import ConfigManager
from weather_client import WeatherClient


def print_current_weather(client: WeatherClient, city: str) -> None:
    try:
        weather = client.get_current(city)
        print(f"Aktuelles Wetter in {weather['city']}:")
        print(f"  Temperatur: {weather['temperature']} °C")
        print(f"  Luftfeuchtigkeit: {weather['humidity']} %")
        print(f"  Wind: {weather['wind_speed']} m/s")
        print(f"  Bedingungen: {weather['description']}")
    except Exception as e:
        print(f"Fehler beim Abrufen des Wetters für {city}: {e}")

def print_forecast(client: WeatherClient, city: str) -> None:
    try:
        forecast = client.get_forecast(city)
        print(f"Wettervorhersage für {city}:")
        for entry in forecast:
            print(f"{entry['date']}: {entry['temperature']} °C, {entry['description']}")
    except Exception as e:
        print(f"Fehler beim Abrufen der Wettervorhersage für {city}: {e}")

