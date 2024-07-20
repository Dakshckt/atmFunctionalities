import tkinter 
from tkinter.ttk import *

def frame1Func(frame):
    loginLabel = Label(frame , text="Enter Your credit card credintials")
    loginLabel.grid(row=0 , column=0 , columnspan=2 , pady=20)

    usernameLabel = Label(frame , text="Enter credit card Number :")
    usernameLabel.grid(row=1 , column=0 , padx=25 , pady=15)
    usernameEntry = Entry(frame , width=20)
    usernameEntry.grid(row=1 , column=1 , padx=25 , pady=15)

    passwordLabel = Label(frame , text="Enter the pin code : ")
    passwordLabel.grid(row=2 , column=0 , padx=25 , pady=15)
    passwordEntry = Entry(frame , width=20 , show='*')
    passwordEntry.grid(row=2 , column=1 , padx=25 , pady=15)

    return usernameEntry , passwordEntry

