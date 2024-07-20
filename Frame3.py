import tkinter
from tkinter.ttk import *

def frame3Func(frame):
    balanceLabel = Label(frame , text="Balance Checking")
    balanceLabel.grid(row=0 , column=0 , columnspan=2 , pady=15)

    pinText = Label(frame , text="Enter your pin : ")
    pinText.grid(row=1 , column=0 , padx=25 , pady=15)

    pinEntry = Entry(frame , width=20 , show='*')
    pinEntry.grid(row=1 , column=1 , padx=25 , pady=15)

    return pinEntry