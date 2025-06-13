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
            print(f"{entry['date']}: {entry['temp']} °C, {entry['description']}")
    except Exception as e:
        print(f"Fehler beim Abrufen der Wettervorhersage für {city}: {e}")

def main():
    parser = argparse.ArgumentParser(
        prog="weather_app",
        description="CLI Weather App – Aktuelles Wetter & 5-Tage-Vorhersage"
    )
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-c", "--current",
        metavar="STADT",
        help="Zeigt aktuelles Wetter für STADT"
    )
    group.add_argument(
        "-f", "--forecast",
        metavar="STADT",
        help="Zeigt 5-Tage-Vorhersage für STADT"
    )
    group.add_argument(
        "--add",
        metavar="STADT",
        help="Fügt STADT als Favoriten hinzu"
    )
    group.add_argument(
        "--remove",
        metavar="STADT",
        help="Entfernt STADT aus Favoriten"
    )
    group.add_argument(
        "--list",
        action="store_true",
        help="Listet alle Favoriten-Städte auf"
    )
    parser.add_argument(
        "--setkey",
        metavar="API_KEY",
        help="Speichert den OpenWeatherMap-API-Key"
    )

    args = parser.parse_args()

    cfg = ConfigManager()

    if args.setkey:
        cfg.set_api_key(args.setkey)
        print("API-Key gespeichert.")
        sys.exit(0)

    if args.add:
        city = args.add.strip()
        if cfg.add_favorite(city):
            print(f"Stadt '{city}' zu Favoriten hinzugefügt.")
        else:
            print(f"Stadt '{city}' war bereits in den Favoriten oder ungültig.")
        sys.exit(0)

    if args.remove:
        city = args.remove.strip()
        if cfg.remove_favorite(city):
            print(f"Stadt '{city}' aus Favoriten entfernt.")
        else:
            print(f"Stadt '{city}' war nicht in den Favoriten.")
        sys.exit(0)

    if args.list:
        favs = cfg.get_favorites()
        if not favs:
            print("Keine Favoriten-Städte gespeichert.")
        else:
            print("Favoriten-Städte:")
            for idx, city in enumerate(favs, start=1):
                print(f"  {idx}. {city}")
        sys.exit(0)

    api_key = cfg.get_api_key()
    if not api_key:
        print("Kein API-Key gefunden. Bitte zuerst mit '--setkey DEIN_KEY' setzen.")
        sys.exit(1)
    client = WeatherClient(api_key)

    if args.current:
        print_current_weather(client, args.current)
    elif args.forecast:
        print_forecast(client, args.forecast)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()