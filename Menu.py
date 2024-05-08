from tkinter import *
import getpass
from datetime import date
import calendar
from sys import exit
userName = getpass.getuser()
thisDate = date.today()
thisDateName = calendar.day_name[thisDate.weekday()]

def window_boot():
        #start
        window=Tk()
        #config
        window.title(userName + "'s Menu")
        window.configure(background="blue")
        #functions
        def click():
                entered_text=textentry.get() #collects text from entry box
                output.delete(0.0, END)
                try:
                        definition = dict1[entered_text.lower()]
                except:
                        definition = "That's not a day of the week, try again."
                output.insert(END, definition)
        def close_window():
                window.destroy()
                menu()
        #content section 1
        photo1 = PhotoImage(file="calendar.png")
        Label (window, image=photo1, bg="black") .grid(row=0, column=0, sticky=W)
        Label (window, text=userName + ", what day is it?", bg="blue", fg="red", font="none 12 bold") .grid(row=1,column=0,sticky=W+E)

        #entries
        textentry = Entry(window, width=20, bg="red")
        textentry.grid(row=2,column=0,sticky=W+E)

        #buttons
        Button(window, text="SUBMIT", width=6, command=click) .grid(row=3,column=0,sticky=W+E)

        #text box
        output = Text(window, width=75, height=6, wrap=WORD, background="red")
        output.grid(row=5, column=0, columnspan=2, sticky=W+E)

        #dictionary
        dict1 = {
                "monday": "Incorrect.",
                "tuesday": "Incorrect.",
                "wednesday": "Incorrect.",
                "thursday": "Incorrect.",
                "friday": "Incorrect.",
                "saturday": "Incorrect.",
                "sunday": "Incorrect.",
                thisDateName.lower(): "Correct."
                }
        #exit label
        Button(window, text="Exit", width=14, command=close_window) .grid(row=7,column=0,sticky=W+E)

        #end
        window.mainloop()
def menu():
        print("Welcome, \n 1. Boot GUI Menu \n 2. Print Hello World \n 3. Exit Console Menu \n")
        choice = input()
        
        if choice == "1":
                window_boot()
                menu()
        if choice == "2":
                print("Hello World!")
                input()
                menu()
        if choice == "3":
                exit()

menu()