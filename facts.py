import requests
import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox

root = Tk()

url = "https://numbersapi.p.rapidapi.com/6/21/date"

factslist1_frm = Frame(master=root, width=100, height=100)
factslist1_frm.pack(side=TOP, fill=BOTH, expand=True)

factslist2_frm = Frame(master=root, width=100, height=100)
factslist2_frm.pack(side=BOTTOM, fill=BOTH, expand=True)

facts1_lbl = Label(master=factslist1_frm, text="Output in dictionary format!")
facts1_lbl.grid(row=0, column=0, padx=5, pady=5)

facts2_lbl = Label(master=factslist2_frm, text="Weight in string formats!")
facts2_lbl.grid(row=0, column=0, padx=5, pady=5)

def interestingfacts1():

	querystring = {"fragment":"true", "json":"true"}

	headers = {
		"X-RapidAPI-Key": "21fffb200emsheb8fb5c5a163ee8p1cc778jsncd646d16dd29",
		"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
	}

	response1 = requests.request("GET", url, headers=headers, params=querystring)
	fact1 = response1.text
	
	interestingfacts1_lbl.config(text="Interesting facts: {}".format(fact1))
	
def interestingfacts2():

	querystring = {"fragment":"true", "json":"true"}

	headers = {
		"X-RapidAPI-Key": "21fffb200emsheb8fb5c5a163ee8p1cc778jsncd646d16dd29",
		"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
	}

	response2 = requests.request("GET", url, headers=headers)
	fact2= response2.text

	interestingfacts2_lbl.config(text="Interesting facts: {}".format(fact2))

interestingfacts1_lbl = Label(master=factslist1_frm, text="", width=175)
interestingfacts1_btn = Button(master=factslist1_frm, width=35, text="Click on me and get a new interesting fact", command=interestingfacts1)

interestingfacts1_lbl.grid(row=1, column=0, padx=5, pady=5)
interestingfacts1_btn.grid(row=2, column=0, padx=5, pady=5)

interestingfacts2_lbl = Label(master=factslist2_frm, text="", width=175)
interestingfacts2_btn = Button(master=factslist2_frm, width=35, text="Click on me and get a new interesting fact", command=interestingfacts2)

interestingfacts2_lbl.grid(row=1, column=0, padx=5, pady=5)
interestingfacts2_btn.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()