from time import *
import random
import os
import json 

file = "OTP.json"
MAX_TRIES = 3
MAX_TIME = 10


class OTP:
    def __init__(self, filename: str):
        self.filename = filename
        self.OTP = self.LoadOTP()

    def LoadOTP(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r") as f:
            return json.load(f)

    def SaveOTP(self):
        with open(self.filename, "w") as f:
            json.dump(self.OTP, f, indent=2, sort_keys=True)

    def otpLogic(self):
        email = input("Enter Email: ")

        if email in self.OTP:
            print("Email already exists.")
            return

        otp = random.randint(1000, 9999)
        created = time()

        print(f"Sending OTP to {email}")
        sleep(2.4)
        print(f"OTP has been sent to {email}")

        self.OTP[email] = {
            "otp": otp,
            "time": created,
            "tries": 0
        }

        self.SaveOTP()

        record = self.OTP[email]

        while True:
            
            if time() - record["time"] > MAX_TIME:
                print("OTP expired.")
                del self.OTP[email]
                self.SaveOTP()
                return

            
            if record["tries"] >= MAX_TRIES:
                print("Too many attempts.")
                del self.OTP[email]
                self.SaveOTP()
                return

            user = input("Enter OTP or type 'resend': ").strip()

            if user.lower() == "resend":
                if time() - record["time"] < MAX_TIME:
                    print("Please wait before resending.")
                    continue

                new_otp = random.randint(1000, 9999)
                record["otp"] = new_otp
                record["time"] = time()
                record["tries"] = 0
                self.SaveOTP()

                print("OTP resent.")
                continue

            if not user.isdigit():
                print("OTP must be numbers only.")
                continue

            if int(user) != record["otp"]:
                record["tries"] += 1
                self.SaveOTP()
                print(f"Incorrect OTP ({record['tries']} / {MAX_TRIES})")
                continue
            print("Access granted.")
            del self.OTP[email]
            self.SaveOTP()
            return


def main():
    manager = OTP(file)
    print("Quit")

    while True:
        manager.otpLogic()
        choice = input("Do u want to quit?: ")

        if choice.lower() in ("yes", "y"):
            break



main()

