import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y(for YES) / N(for NO) ." % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn=="N":
            return "Word does not exist in Data"
    else:
        return "Word does not exist in Data"

word=input("Enter a word: ")

output=translate(word)

for sentence in output:
    print(sentence)
