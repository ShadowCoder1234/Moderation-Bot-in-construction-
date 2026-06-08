import os 
import json


file =  "bad_words.json"


class MODERATOR_BOT():
    def __init__(self, file, text):
        self.file = file
        self.text = text
        self.load = self.Load()
    def Load(self):
        if not os.path.exists(self.file):
            return {
                "idiot": 20,
                "hacker": 50,
                "malware": 90
            }
        with open(self.file, "r+") as f:
            return json.load(f)
    def Save(self):
        with open(self.file, "w") as f:
            json.dump(f, indent=2, sort_keys= True)
        
        




    
        
        
