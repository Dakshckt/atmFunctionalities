import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from Frame1 import frame1Func
from Frame2 import frame2Func
from Frame3 import frame3Func
from Frame4and5 import frame4and5Func
from Frame6 import frame6Func
from Frame7 import frame7Func
from AllFunc import allFunc
from Database import selectData , updateData
from Operation import operation

base = tk.Tk()
base.geometry("400x500")
base.title("ATM")

nb = Notebook(base)

frame1 = Frame(nb)
frame2 = Frame(nb)
frame3 = Frame(nb)
frame4 = Frame(nb)
frame5 = Frame(nb)
frame6 = Frame(nb)
frame7 = Frame(nb)
frame8= Frame(nb)
frame9= Frame(nb)

USERNAME = ''
CREDIT = ''
PIN = ''
AMOUNT = ''

def init():
    nb.add(frame1 , text="Login")
    nb.add(frame2 , text="Operation")
    nb.add(frame3 , text="Balance Display")
    nb.add(frame4 , text="Withdraw")
    nb.add(frame5 , text="Deposit")
    nb.add(frame6 , text="Details")
    nb.add(frame7 , text="Remarks Display")
    nb.add(frame8 , text="Thank you")
    nb.add(frame9 , text="Crash")
    nb.forget(frame2)
    nb.forget(frame3)
    nb.forget(frame4)
    nb.forget(frame5)
    nb.forget(frame6)
    nb.forget(frame7)
    nb.forget(frame8)
    nb.forget(frame9)  # Extra frame to detect error

def getname():
    global USERNAME , PIN , CREDIT , AMOUNT
    username , pin , credit , amount = obj.checkUser(nb , usernameEntry , passwordEntry , frame2 , frame1)
    USERNAME , PIN , CREDIT , AMOUNT = username , pin , credit , amount

obj = allFunc()

usernameEntry , passwordEntry = frame1Func(frame1)
loginButton = Button(frame1 , text="Move Froward" , width=20 , command=lambda : getname())
loginButton.grid(row=3 , column=1 , padx=25 , pady=15)
frame1.pack(fill=tk.BOTH , expand=True)

frame2Func(frame2)
checkLabel = Label(frame2 , text="Check Balance")
checkLabel.grid(row=1 , column=0 , padx=25 , pady=15)
checkButton = Button(frame2 , text="Check Amount" , width=20 , command=lambda : obj.checkAmount(nb , frame3 , frame2))
checkButton.grid(row=1 , column=1 , padx=25 , pady=15)
widthdrawLabel = Label(frame2 , text="Withdraw Balance")
widthdrawLabel.grid(row=2 , column=0 , padx=25 , pady=15)
widthdrawButton = Button(frame2 , text="Withdraw" , width=20 , command=lambda : obj.withdraw(nb , frame4 , frame2))
widthdrawButton.grid(row=2 , column=1 , padx=25 , pady=15)
depositLabel = Label(frame2 , text="Deposit Balance")
depositLabel.grid(row=3 , column=0 , padx=25 , pady=15)
depositButton = Button(frame2 , text="Deposit" , width=20 , command=lambda : obj.deposit(nb , frame5 , frame2))
depositButton.grid(row=3 , column=1 , padx=25 , pady=15)
frame2.pack(fill=tk.BOTH , expand=True)

pinEntry = frame3Func(frame3)
balanceButton = Button(frame3 , text="Check" , width=20 , command=lambda : obj.balance( pinEntry , frame6Func , nb , frame6 , frame3 ,  USERNAME , CREDIT , PIN , AMOUNT))
balanceButton.grid(row=2 , column=1 , padx=25 , pady=15)
frame3.pack(fill=tk.BOTH , expand=True)

amountEntryFrame4 , pinEntryFrame4 = frame4and5Func(frame4 , "WithDraw")
withdrawButton = Button(frame4 , text="WithDraw" , command=lambda : operation(amountEntryFrame4 , pinEntryFrame4 , USERNAME , CREDIT , PIN , frame4 , frame7 , frame1 , nb , 1))
withdrawButton.grid(row=3 , column=1 , padx=25 , pady=15)
frame4.pack(fill=tk.BOTH , expand=True)

amountEntryFrame5 , pinEntryFrame5 = frame4and5Func(frame5 , "Deposit")
depositButton = Button(frame5 , text="Deposit" , command=lambda : operation(amountEntryFrame5 , pinEntryFrame5 , USERNAME , CREDIT , PIN , frame5 , frame7 , frame1 , nb , 0))
depositButton.grid(row=3 , column=1 , padx=25 , pady=15)
frame5.pack(fill=tk.BOTH , expand=True)

closeButton = Button(frame6 , text="Close" , width=15 , command=lambda : obj.close(nb , frame8 , frame6))
closeButton.grid(row=4 , column=1 , padx=25 , pady=15)
frame6.pack(fill=tk.BOTH , expand=True)

frame7Func(frame7)
yesButton = Button(frame7 , text="Yes" , width=20 , command=lambda : obj.yesCmd(nb , frame3 , frame7))
yesButton.grid(row=1 , column=0 , padx=25 , pady=15)
noButton = Button(frame7 , text="No" , width=20 , command=lambda : obj.noCmd(nb , frame8 , frame7))
noButton.grid(row=1 , column=1 , padx=25 , pady=15)
frame7.pack(fill=tk.BOTH , expand=True)

thankLabel = Label(frame8 , text="Thank You" , font=("Arial" , 30))
thankLabel.pack(pady=25)
thankButton = Button(frame8 , text="Go Back" , command= lambda : obj.back(init))
thankButton.pack(pady=25)
frame8.pack(fill=tk.BOTH , expand=True)

crashLabel = Label(frame9 , text="Error in Transaction")
crashLabel.pack(pady=25)
crashButton = Button(frame9 , text="Go Back" , command= lambda : obj.back(init))
crashButton.pack(pady=25)
frame9.pack(fill=tk.BOTH , expand=True)

nb.pack(fill=tk.BOTH , expand=True , padx=10 , pady=5)

init()

base.mainloop()