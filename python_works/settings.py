import json
import os

FILE = "settings.json"


class Settings:
    def __init__(self, filename):
        self.filename = filename
        self.settings = self.load_settings()

    def load_settings(self):
        default_settings = {
            "user": "Aarav",
            "theme": "dark",
            "debug": True,
            "volume": 50,
            "notifications": True
        }

        if not os.path.exists(self.filename):
            self._write_file(default_settings)
            return default_settings

        with open(self.filename, "r") as f:
            return json.load(f)

    def _write_file(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2, sort_keys=True)

 
    def show_settings(self):
        print("\nCurrent Settings:")
        for key, value in self.settings.items():
            print(f"{key} => {value}")

   
    def update_setting(self, key, raw_value):
        if key not in self.settings:
            print("Setting not found ")
            return

        value = self._convert_type(raw_value)
        self.settings[key] = value
        self._write_file(self.settings)
        print("Setting updated ")


    def _convert_type(self, raw):
        raw = raw.strip().lower()

        if raw == "true":
            return True
        if raw == "false":
            return False
        if raw.isdigit():
            return int(raw)

        return raw


def main():
    manager = Settings(FILE)

    while True:
        print("\n1. Show Settings")
        print("2. Update Setting")
        print("3. Exit")

        choice = input("Choose (1/2/3): ")

        if choice == "1":
            manager.show_settings()

        elif choice == "2":
            key = input("Enter setting name: ").strip().lower()
            value = input("Enter new value: ")
            manager.update_setting(key, value)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice ")


main()
