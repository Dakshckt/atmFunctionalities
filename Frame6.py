import tkinter
from tkinter.ttk import *

def frame6Func(frame , user , credit , amount):
    displayLabel = Label(frame , text="Following is the balance and user Details")
    displayLabel.grid(row=0 , column=0 , columnspan=2 , pady=15)

    username = user
    usercredit = credit
    useramount = amount

    name = Label(frame , text=f"Name : {username}")
    name.grid(row=1 , column=0 , pady=15)

    creditCard = Label(frame , text=f"Credit Card : {usercredit}")
    creditCard.grid(row=2 , column=0 ,padx=15, pady=15)

    amount = Label(frame , text=f"Amount : {useramount}")
    amount.grid(row=3 , column=0 , pady=15)