import json
import difflib

from difflib import get_close_matches

data=json.load(open("data.json")) #Loads Dictory Data

#Returning the Meaning
def meaning(word):
    word=word.lower()
    if word in data.keys(): 
        return data[word]
    elif word.title() in data.keys(): #Looking for Titles
        return data[word.title()]
    elif word.upper() in data.keys(): #Looking for Words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0: #Getting the Closest Match
        print("Did you mean %s instead?" %get_close_matches(word,data.keys())[0])
        choice=input("Enter Y for Yes and N for No: ")
        choice=choice.upper()
        if choice=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif choice=="N":
            return word_options(word) #Showing Word Options 
        else:
            return "We Cannot Understand your Query"
    else:
        return "The Word Doesn't Exist! Kindly Recheck the Same."

def word_options(word_check): #Printing all Possible Words from the Query
    print("Do you mean anyone of these?\n")
    for option in get_close_matches(word_check,data.keys()):
        print(option)
    recheck=input("Enter Y for Yes and N for No: ")
    if recheck=="Y":
        new_word=input("Enter Word: ")
        new_word.lower()
        return data[new_word]
    elif recheck=="N":
        return "The Word Doesn't Exist! Kindly Recheck the Same"
    else:
        return "We Didn't Understand your Query"

w=input("Enter Word: ")

output=meaning(w)

# 'if' is used for words with multiple meanings
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)