import random
from datetime import datetime
import time
from zoneinfo import ZoneInfo
import string


def greet():
    try:
        name = input("Please enter your name: ")
        greetings = [
            f"Hello, {name}. How may I help you?",
            f"Hi, {name}. How may I assist you?"
        ]
        return random.choice(greetings)
    except ValueError:
        print("Error")
        return None


greet_message = greet()
print(greet_message)


def ask():
    return input("> ")

def answer_time(asked):
    valid = ["whats the time", "time"]

    if asked.lower() in valid:
        current_time = datetime.now(ZoneInfo('Asia/Kolkata'))
        time_format = current_time.strftime("%H: %M: %S %p")
        print(time_format)
        return True      
    
    return False        

def answer_math(asked):
    queries = ["i want to do math", "math", "calc", "calculator"]

    if asked.lower() in queries:
        print("Alright, let's do it.")
        
        try:
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))
            operator = input("Enter your operator (+, -, *, /): ")
            
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: cannot divide by zero")
                    return True
                result = num1 / num2
            else:
                print("Invalid operator.")
                return True

            print("Calculating..")
            time.sleep(0.5)
            print(result)
            return True

        except ValueError:
            print("Cannot put words.")
            return True
    
    return False   

def answer_joke(asked):
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the chicken go to the séance? To get to the other side.",
        "What did the ocean say to the pirate? Nothing, it just waved.",
        "What kind of doctor fixes broken websites? A URLologist.",
        "How do trees get on the Internet? They log in."
    ]
    triggers = ["joke", "tell me a joke", "funny", "make me laugh"]

    if asked.lower() in triggers:
        joke_choice = random.choice(jokes)
        print(joke_choice)
        return True
    
    return False

def gen_password(asked):

    t  = ["gen", "make a password", "generate a password"]

    if asked.lower() in t:
        length = int(input("Enter length: "))

        chara = string.ascii_letters + string.digits + string.punctuation
        password = ""

        for i in range(length):
            password += random.choice(chara)   

        print(f"Your password is: {password}")
        return True
    
    return False

        
while True:
    asked = ask()

   
    if asked.lower() == "exit":
        print("Goodbye!")
        break

    elif answer_math(asked):
        continue

    elif answer_time(asked):
        continue
    elif answer_joke(asked):
        continue

    elif gen_password(asked):
        continue

    else:
        print("This function is not availble at the moment.")


    

  