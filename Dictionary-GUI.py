import tkinter
from tkinter import *
import difflib
import json

#from difflib import get_close_matches

data=json.load(open("E:\Programs\Python\Interactive-Dictionary\data.json"))

root=Tk()
root.title("Dictionary")

word_meaning="Meaning will be displayed here."
word=tkinter.StringVar()

label_word=Label(root, text="Enter Word")
label_word.grid(row=0)

enter_word=Entry(root, width=26, textvariable=word)
enter_word.grid(row=0,column=1)
enter_word.focus_set()

output_label=Label(root, text="Meaning")
output_label.grid(row=2, column=1)

#Returning the Meaning
def meaning():
    global enter_word
    global word_meaning
    word=enter_word.get()
    word=word.lower()
    if word in data.keys(): 
        word_meaning=data[word]
    elif word.title() in data.keys(): #Looking for Titles
        word_meaning=data[word.title()]
    elif word.upper() in data.keys(): #Looking for Words like USA or NATO
        word_meaning=data[word.upper()]
    else:
        word_meaning="The Word Doesn't Exist! Kindly Recheck the Same."

    output_label.configure(text=word_meaning)

search_button=Button(root, text="  Search Word", command=meaning)
search_button.grid(row=0, column=3)

design=Label(root, text="Design & Developed by Simardeep Singh")
design.grid(row=6, column=1)

root.mainloop()