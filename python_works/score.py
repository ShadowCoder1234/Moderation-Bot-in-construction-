import json
import os
file = "score.json"

class ScoreManager:
    def __init__(self, filename):
        self.filename = filename
        self.scores = self.loadScores()

    def loadScores(self):
        if not os.path.exists(self.filename):
            return {
                "Aarav": 23
            }
        with open(self.filename, "r") as f:
            return json.load(f)

            
        
    def SaveScores(self):
        with open(self.filename, "w") as f:
            json.dump(self.scores, f, indent=2, sort_keys=True)
            
    def updateScores(self):
        try:
            name = input("Enter name: ")
            score = int(input("How many scores u want to update?: "))
            if name not in self.scores:
                print("Person does not exist")
                return
            scoreChoice = input("Do u want to increase or decrease?: ")
            if scoreChoice.lower() == "increase":
                self.scores[name] += score
            elif scoreChoice.lower() == "decrease":
                self.scores[name] -= score
            print("Score updated.")
            self.SaveScores()
        except ValueError:
            print("Invalid number")
            return
        
    def NewUser(self):
        try:
            name = input("Enter name: ")
            score = int(input("Enter score: "))
            if name in self.scores:
                print("Name exists.")
                return
            self.scores[name] = score
            print("Added user to score.json")
            self.SaveScores()
        except ValueError:
            print("Invalid number")
            return
    def deleteUser(self):
        name = input("What name do u want to delete?: ")
        if name in self.scores:
            del self.scores[name]
            self.SaveScores()
            print("Deleted user")
        elif name not in self.scores:
            print("User does not exist.")
            
      
    def showScores(self):
        print("Scores are: ")
        for name, scores in self.scores.items():
            print(f"{name} => {scores}")
   
def main():
    manager = ScoreManager(file)
    
    while True:
        print("1. Update Scores.")
        print("2. See scores.")
        print("3. Enter new user: ")
        print("4. Delete a user.")
        print("5. Quit.")
        choice = input("1/2/3/4/5: ")
        
        if choice == "1":
            manager.updateScores()
        elif choice == "2":
            manager.showScores()
        elif choice == "3":
            manager.NewUser()
        elif choice == "4":
            manager.deleteUser()
        elif choice == "5":
            break
        else:
            print("The function does not exist")
main()

