import tkinter as tk
from tkinter import messagebox
from Database import selectData

class allFunc:
    def checkAmount(self , nb, frame3 , frame2):
        nb.add(frame3 , text="Balance")
        nb.forget(frame2)

    def withdraw(self , nb , frame4 , frame2):
        nb.add(frame4 , text="Withdraw Amount")
        nb.forget(frame2)

    def deposit(self, nb , frame5 , frame2):
        nb.add(frame5 , text="Deposit Amount")
        nb.forget(frame2)

    def close(self , nb , frame8 , frame6):
        nb.add(frame8 , text="Thanks")
        nb.forget(frame6)

    def yesCmd(self , nb , frame3 , frame7):
        nb.add(frame3 , text="Balance")
        nb.forget(frame7)

    def noCmd(self , nb , frame8 , frame7):
        nb.add(frame8 , text="Thanks")
        nb.forget(frame7)
    
    def back(self , init):
        init()
    
    def checkUser(self , nb , usernameEntry , passwordEntry , frame2 , frame1):
        credit = usernameEntry.get()
        try:
            pin = int(passwordEntry.get())
        except Exception as err:
            pass

        usernameEntry.delete(0 , tk.END)
        passwordEntry.delete(0 , tk.END)
        result = selectData()
        run = False
        for val in result:
            if val['credit'] == credit and val['pin'] == pin:
                global USERNAME , PIN , CREDIT , AMOUNT
                USERNAME = val['name']
                PIN = val['pin']
                CREDIT = val['credit']
                AMOUNT = val['amount']
                run = True
                break

        if run == True:
            nb.add(frame2 , text="Operation")
            nb.forget(frame1)
            return USERNAME , PIN , CREDIT , AMOUNT
        else:
            messagebox.showerror("Error","User Does not exsist!")
    

    def balance(self , pinEntry , frame6Func , nb , frame6 , frame3 , USERNAME , CREDIT , PIN , AMOUNT):
        try:
            password = int(pinEntry.get())
            pinEntry.delete(0 , tk.END)
            if password == PIN:
                result = selectData()
                for val in result:
                    if val['name'] == USERNAME and val['credit'] == CREDIT and val['pin'] == PIN:
                        AMOUNT = val['amount']
                        frame6Func(frame6 , USERNAME , CREDIT , AMOUNT)
                        nb.add(frame6 , text="Details")
                        nb.forget(frame3)
            else:
                messagebox.showerror("Error","Invalid Pin")

        except Exception as err:
            pinEntry.delete(0 , tk.END)
            messagebox.showerror("Error","Invalid Pin")