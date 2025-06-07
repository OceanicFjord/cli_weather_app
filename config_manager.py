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
        # Datei-Existenz-Check und JSON-Laden
        if os.path.isfile(self.config_path):
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"[ConfigManager] WARNUNG: {self.config_path} ungültig oder nicht lesbar ({e}).")
                self._save()
            self.config["api_key"] = data.get["api_key", ""]
            self.config["favorites"] = data.get["favorites", []]
            return
        else:
            self._save()
            return

