# CLI Weather App

**CLI Weather App** ist eine schlanke Kommandozeilen-Anwendung, mit der du dir jederzeit das aktuelle Wetter und eine 5-Tage-Vorhersage (jeweils 12:00 Uhr) für beliebige Städte anzeigen lassen kannst. Über eine integrierte Favoritenverwaltung legst du deine meistgenutzten Orte einmal an und greifst sie dann mit einem einzigen Befehl ab.

## Features

- **API-Key per CLI**: Nie im Code gespeichert, lokal in `config.json` abgelegt  
- **Favoriten verwalten**: Städte über die Kommandozeile hinzufügen, entfernen und listen  
- **Aktuelles Wetter**: Temperatur, Luftfeuchtigkeit, Windgeschwindigkeit und Bedingungen  
- **5-Tage-Vorhersage**: Tageswerte („Mittag“) für die nächsten fünf Tage  
- **Modulare Klassenstruktur**:  
  - `ConfigManager` für Konfigurationsdatei (`config.json`)  
  - `WeatherClient` für HTTP-Requests an OpenWeatherMap  
  - `weather_app.py` als übersichtliches CLI-Interface (mit `argparse`)
  
## Installation

1. Repository klonen  
   ```bash
   git clone https://github.com/DEIN_USER/cli_weather_app.git
   cd cli_weather_app
   ```

2. Virtuelle Umgebung anlegen & aktivieren
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate   # Windows: .venv\Scripts\activate
    ```

3. Abhängigkeiten installieren
    ```bash
    pip install -r requirements.txt
    ```

4. config.json ignorieren (wird automatisch angelegt)
    ```bash
    echo "config.json" >> .gitignore
    ```

## Nutzung

1. API-Key setzen
    ```bash
    python weather_app.py --setkey DEIN_OPENWEATHERMAP_API_KEY
    ```

2. Favoriten verwalten
    - Hinzufügen: 
        ```bash
        python weather_app.py --add Berlin
        ```
    
    - Entfernen:
        ```bash
        python weather_app.py --remove Berlin
        ```
    
    - Auflisten:
        ```bash
        python weather_app.py --list
        ```

3. Wetterabfragen
    - Aktuelles Wetter:
    ```bash
    python weather_app.py --current Berlin
    ```

    - 5-Tage-Vorhersage:
    ```bash
    python weather_app.py --forecast Berlin
    ```


## Beispiel

```bash
$ python weather_app.py --setkey abc123
API-Key gespeichert.

$ python weather_app.py --add Berlin
Stadt 'Berlin' zu Favoriten hinzugefügt.

$ python weather_app.py --list
Favoriten-Städte:
  1. Berlin

$ python weather_app.py --current Berlin
Aktuelles Wetter in Berlin:
  Temperatur: 18.3 °C
  Luftfeuchtigkeit: 62 %
  Wind: 5.4 m/s
  Bedingungen: Leichter Regen

$ python weather_app.py --forecast Berlin
5-Tage-Vorhersage für Berlin:
  2025-06-10: 22.1 °C, Klarer Himmel
  2025-06-11: 19.7 °C, Leichter Regen
  2025-06-12: 21.4 °C, Bewölkt
  2025-06-13: 20.0 °C, Regenschauer
  2025-06-14: 23.8 °C, Sonnig
```


## Lizenz
MIT License – siehe [LICENSE](LICENSE) für Details.