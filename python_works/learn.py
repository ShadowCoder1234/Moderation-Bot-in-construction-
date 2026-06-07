import json 
import os
import asyncio as a
file = "contacts.json"
CURRENT_VERSION = 2


def migrate_v1_to_v2(old_data):
    new_data = {}

    for name, phone in old_data.items():
        new_data[name] = {
            "phone": phone,
            "email": ""
        }

    return new_data


class ContactsManager:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.loadContacts()

    def loadContacts(self):
        if not os.path.exists(self.filename):
            default = {
                "version": CURRENT_VERSION,
                "data": {}
            }
            with open(self.filename, "w") as f:
                json.dump(default, f, indent=2)
            return default["data"]

        with open(self.filename, "r") as f:
            raw = json.load(f)

        if "version" not in raw:
            raw = {
                "version": 1,
                "data": raw
            }

        if raw["version"] == 1:
            print("Migrating contacts from v1 to v2")
            migrated_data = migrate_v1_to_v2(raw["data"])
            raw = {
                "version": 2,
                "data": migrated_data
            }
            with open(self.filename, "w") as f:
                json.dump(raw, f, indent=2)

        return raw["data"]

    def saveContacts(self):
        payload = {
            "version": CURRENT_VERSION,
            "data": self.contacts
        }
        with open(self.filename, "w") as f:
            json.dump(payload, f, indent=2)

    def AddContact(self):
        name = input("Enter name: ").strip().capitalize()
        email = input("Enter email (optional): ").strip()
        phone = input("Enter phone number: ").strip()

        if not phone.isdigit():
            print("Phone number must contain only digits.")
            return

        if len(phone) != 10:
            print("Phone number must be exactly 10 digits.")
            return

        if name in self.contacts:
            print("Name already exists.")
            return

        self.contacts[name] = {
            "phone": phone,
            "email": email
        }
        self.saveContacts()
        print("Contact added ")

    def DeleteContacts(self):
        name = input("Enter name: ").strip().capitalize()

        if name not in self.contacts:
            print("Cannot find name.")
            return

        del self.contacts[name]
        self.saveContacts()
        print("Contact deleted ")

    def SeeContacts(self):
        if not self.contacts:
            print("No contacts.")
            return

        print("Your contacts:")
        for name, info in self.contacts.items():
            print(f"{name} => {info['phone']} | {info['email']}")



def main():
    manager = ContactsManager(file)

    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. See Contacts")
        print("4. Quit")

        choice = input("Enter (1/4): ")

        if choice == "1":
            manager.AddContact()
        elif choice == "2":
            manager.DeleteContacts()
        elif choice == "3":
            manager.SeeContacts()
        elif choice == "4":
            break
        else:
            print("Function not available.")
    

main()

