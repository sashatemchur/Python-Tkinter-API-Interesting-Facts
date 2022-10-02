import requests
import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox

root = Tk()

url = "https://numbersapi.p.rapidapi.com/6/21/date" # Makes a url with interesting facts from history

factslist1_frm = Frame(master=root, width=100, height=100) # Creates a window where the url appears
factslist1_frm.pack(side=TOP, fill=BOTH, expand=True)

factslist2_frm = Frame(master=root, width=100, height=100) # Creates a window where the url appears
factslist2_frm.pack(side=BOTTOM, fill=BOTH, expand=True)

facts1_lbl = Label(master=factslist1_frm, text="Output in dictionary format!") # Creates a term in which it is indicated in which format the url is displayed
facts1_lbl.grid(row=0, column=0, padx=5, pady=5)

facts2_lbl = Label(master=factslist2_frm, text="Weight in string formats!") # Creates a term in which it is indicated in which format the url is displayed
facts2_lbl.grid(row=0, column=0, padx=5, pady=5)


def interestingfacts1():
	# Makes interesting facts about the dictionary
	querystring = {"fragment":"true", "json":"true"} # Specifies all parameters in changes

	headers = {
		"X-RapidAPI-Key": "21fffb200emsheb8fb5c5a163ee8p1cc778jsncd646d16dd29",
		"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
	} # Makes interesting facts 

	response1 = requests.request("GET", url, headers=headers, params=querystring) # Makes interesting facts about the dictionary
	fact1 = response1.text # Translates url text and saves in changes 
	
	interestingfacts1_lbl.config(text="Interesting facts: {}".format(fact1)) # Inserts the url in the string in the form of a dictionary
	
 
def interestingfacts2():
	# Makes interesting facts in the form of a deadline
	querystring = {"fragment":"true", "json":"true"} # Specifies all parameters in changes 

	headers = {
		"X-RapidAPI-Key": "21fffb200emsheb8fb5c5a163ee8p1cc778jsncd646d16dd29",
		"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
	} # Makes interesting facts 

	response2 = requests.request("GET", url, headers=headers) # Makes interesting facts in the form of a deadline
	fact2= response2.text # Translates url text and saves in changes

	interestingfacts2_lbl.config(text="Interesting facts: {}".format(fact2)) # Inserts the url as a string into the string

interestingfacts1_lbl = Label(master=factslist1_frm, text="", width=175) # Makes the term in which the url is inserted
interestingfacts1_btn = Button(master=factslist1_frm, width=35, text="Click on me and get a new interesting fact", command=interestingfacts1) # Makes a button that displays text from the url

interestingfacts1_lbl.grid(row=1, column=0, padx=5, pady=5)
interestingfacts1_btn.grid(row=2, column=0, padx=5, pady=5)

interestingfacts2_lbl = Label(master=factslist2_frm, text="", width=175) # Makes the term in which the url is inserted
interestingfacts2_btn = Button(master=factslist2_frm, width=35, text="Click on me and get a new interesting fact", command=interestingfacts2) # Makes a button that displays text from the url

interestingfacts2_lbl.grid(row=1, column=0, padx=5, pady=5)
interestingfacts2_btn.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()