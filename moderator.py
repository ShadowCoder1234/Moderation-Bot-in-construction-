import os
import json
import re


FILE = "bad_words.json"


class ModeratorBot():

    def __init__(self, file):
        self.file = file
        self.bad_words = self.load()

    def load(self):
        if not os.path.exists(self.file):
            return {
                "idiot": 20,
                "hacker": 50,
                "malware": 90
            }

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.bad_words, f, indent=2, sort_keys=True)

    def add(self, word, score):
        word = word.lower()
        self.bad_words[word] = score
        self.save()

    def remove(self, word):
        word = word.lower()

        if word in self.bad_words:
            del self.bad_words[word]
            self.save()

    def normalize(self, text):
        text = text.lower()
        text = re.sub(r"(.)\1+", r"\1", text)  
        text = re.sub(r"\d+", "", text)
        text = re.sub(r"[^\w\s]", "", text)

        return text.split()

    def moderate(self, text):

        score = 0
        detected = []

        words = self.normalize(text)

        for word in words:
            if word in self.bad_words:
                score += self.bad_words[word]
                detected.append(word)

        if score <= 30:
            ability = "Allowed"
        else:
            ability = "Blocked"

        return {
            "score": score,
            "ability": ability,
            "detected": detected
        }


bot = ModeratorBot(FILE)

bot.add("stupid", 25)

result = bot.moderate("You are stuuuuuuupid and an idiot!!")

print(result)
        

        




    
        
        
