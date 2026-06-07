import re

def idk(text):
    bad_words = {
        "idiot": 20,
        "hacker": 50,
        "malware": 90
    }
    SCORE = 0
    Ability = "" 
    detect = []

    text = re.sub(r'[^\w\s]', "", text)
    text = "".join(text.lower())
    text = text.lower()
    text = text.split()

    for t in text:
        if t in bad_words:
            SCORE += bad_words[t]
            detect.append(t)
    
    if SCORE <= 30:
        Ability = "Allowed"
    elif SCORE > 30:
        Ability = "Blocked"
    else:
        Ability = "None"
    
    return{
        'score': SCORE,
        'action': Ability,
        'detected': detect
    }



print(idk("What is this idiot doing"))

