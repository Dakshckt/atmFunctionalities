import tkinter
from tkinter.ttk import *

def frame4and5Func(frame , txt):
    operationLabel = Label(frame , text=txt)
    operationLabel.grid(row=0 , column=0 , columnspan=2 , pady=15)

    amountLabel = Label(frame , text="Enter the amount : ")
    amountLabel.grid(row=1 , column=0 , padx=25 , pady=15)
    amountEntry = Entry(frame , width=20)
    amountEntry.grid(row=1 , column=1 , padx=25 , pady=15)

    pinLabel = Label(frame , text="Enter the pin : ")
    pinLabel.grid(row=2 , column=0 , padx=25 , pady=15)
    pinEntry = Entry(frame , width=20 , show='*')
    pinEntry.grid(row=2 , column=1 , padx=25 , pady=15)

    return amountEntry , pinEntry