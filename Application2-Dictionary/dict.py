#Need to import json to load data file containing lots of words
import json
#This library helps you get the close matches with the entered word which is awesome
from difflib import get_close_matches


data = json.load(open("data.json"))

def dictionary(word):

    word=word.lower()

    if word in data:
        return data[word]
    elif word.title() in data: #incase user enters Delhi as delhi OR India as india
        return data[word.title()]
    elif word.upper() in data: #incase user enters USA as usa
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? \n Enter Y if yes or N if no :" %get_close_matches(word, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist. Please double check it !"
        else:
            return "Sorry ! We didn't get your query.."

    else:
        print("Sorry ! The word doesn't exist..Please check the word again or try something else.")

word=input("Enter a word :")
output = dictionary(word)

if type(output) == list: #If a dictionary occurs while putting no then put it on a list to print the same
    for i in output:
        print(">>>",i)
else:
    print(output)
