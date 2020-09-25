import json
from difflib import get_close_matches

dictionary = json.load(open("1. Word Definition/data/data.json"))

def locate_and_return(w):
    if not w.title():
        w = w.lower()
    else:
        w = w.capitalize()
        
    if w in dictionary:
        return "\n".join(dictionary[w])
    else:
        similar_words = get_close_matches(w, dictionary.keys())
        if(similar_words):
            print("Did you mean {} instead?".format(similar_words[0]))
            confirmation = input("Enter Yes or No:")
            if(confirmation.lower() == "yes" or confirmation.lower() == "y"):
                return "\n".join(dictionary[similar_words[0]])
            else:
                return "Query not found"
        else:
            return "The Word Doesnt Exist"

word = input("Enter The Word: ")
print(locate_and_return(word))