import json
import os


class ConfigManager:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        # Default-Struktur, falls Datei nicht existiert
        self.config = {
            "api_key": "",
            "favorites": []
        }
        self._load_or_create()

    def _load_or_create(self):
        # TODO: Implementiere Datei-Existenz-Check und JSON-Laden
        pass
