import json
import os
from time import sleep as s

file = "data.json"

class PriceChecker:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.loadData()
        self.rates = self.data["rates"]
        self.history = self.data["history"]

    def loadData(self):
        if not os.path.exists(self.filename):
            default = {
                "rates": {
                    "dollar": {"rupee": 90, "dirham": 3.67},
                    "rupee": {"dollar": 1/90},
                    "dirham": {"dollar": 1/3.67}
                },
                "history": {}
            }
            with open(self.filename, "w") as f:
                json.dump(default, f, indent=2)
            return default

        with open(self.filename, "r") as f:
            return json.load(f)

    def saveData(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=2)

    def addHistoryPrice(self):
        print("Welcome to Price Checker")
        s(1)

        frm = input("From currency: ").lower()
        to = input("To currency: ").lower()

        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Amount must be a number")
            return

        if frm not in self.rates or to not in self.rates[frm]:
            print("Conversion not supported")
            return

        result = amount * self.rates[frm][to]
        print(f"{amount} {frm} = {result:.2f} {to}")

        self.history.setdefault(frm, {}).setdefault(to, []).append(result)
        self.saveData()

    def SeePrice(self):
        if not self.history:
            print("No history yet")
            return

        for frm, targets in self.history.items():
            for to, values in targets.items():
                print(f"{frm} → {to} = {values}")

    def AddCurrency(self):
        name = input("New currency name: ").lower()

        if name in self.rates:
            print("Currency already exists")
            return

        self.rates[name] = {}

        print("Enter conversion rates FROM this currency:")
        while True:
            target = input("Convert to (or 'done'): ").lower()
            if target == "done":
                break

            if target == name:
                print("Cannot convert to itself")
                continue

            try:
                rate = float(input(f"1 {name} = ? {target}: "))
            except ValueError:
                print("Rate must be a number")
                continue

            self.rates[name][target] = rate

        self.saveData()
        print("Currency added successfully")

def main():
    manager = PriceChecker(file)

    while True:
        print("\n1. Convert currency")
        print("2. See history")
        print("3. Add currency")
        print("4. Quit")

        choice = input("Choose: ")

        if choice == "1":
            manager.addHistoryPrice()
        elif choice == "2":
            manager.SeePrice()
        elif choice == "3":
            manager.AddCurrency()
        elif choice == "4":
            break
        else:
            print("Invalid option")

main()
