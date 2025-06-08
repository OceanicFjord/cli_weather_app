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

    def _save(self):
        # Öffnet Datei im Schreibmodus und json.dump(self.config)
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"[ConfigManager] FEHLER beim Schreiben der Datei '{self.config_path}': {e}")
    
    def get_api_key(self) -> str:
        return self.config["api_key"]
    
    def set_api_key(self, key: str) -> None:
        # key säubern, in self.config übernehmen, _save() aufrufen
        self.config["api_key"] = key.strip()
        self._save()

    def get_favorites(self) -> list:
        return list(self.config["favorites"])

