import tkinter as tk
from tkinter import messagebox
from Database import selectData , updateData

def operation(amountEntryFrame , pinEntryFrame , USERNAME , CREDIT , PIN , cancelFrame , showFrame , errorFrame , nb , text):
    amountFrame = int(amountEntryFrame.get())
    pinFrame = int(pinEntryFrame.get())
    amountEntryFrame.delete(0 , tk.END)
    pinEntryFrame.delete(0 , tk.END)

    if pinFrame == PIN:
        if amountFrame % 100 == 0:
            if amountFrame < 10000:
                try:
                    result = selectData()
                    for val in result:
                        if val['name'] == USERNAME and val['credit'] == CREDIT and val['pin'] == PIN:
                            if text == 1:
                                actuall_amount = val['amount']
                                new_amount = actuall_amount - amountFrame
                                if new_amount > 1000:
                                    allreadyData = {
                                        'name' : USERNAME,
                                        'credit' : CREDIT,
                                        'pin' : PIN
                                    }
                                    newData = {
                                        'amount':new_amount
                                    }
                                    updateData(allreadyData , newData)
                                    break
                                else:
                                    messagebox.showerror("Error","The balance remains to less check the passbock first")
                                    return True
                            else:
                                actuall_amount = val['amount']
                                new_amount = actuall_amount + amountFrame
                                if new_amount < 1000000:
                                        allreadyData = {
                                            'name' : USERNAME,
                                            'credit' : CREDIT,
                                            'pin' : PIN
                                        }
                                        newData = {
                                            'amount':new_amount
                                        }
                                        updateData(allreadyData , newData)
                                        break
                                else:
                                    messagebox.showerror("Error","The total amount gets more higher check the bank instead")
                                    return True
                    
                    if text == 1:
                        messagebox.showinfo("Done" , "Collect the cash!")
                    else:
                        messagebox.showinfo("Done" , "Transaction Completed")
                    nb.add(showFrame , text="Withdraw")
                    nb.forget(cancelFrame)
                except Exception as err:
                    messagebox.showerror("Error","Error in the transaction process")
                    nb.add(errorFrame , text="Login")
                    nb.forget(cancelFrame)
            else:
                if text == 1:
                    messagebox.showerror("Error","Amount should be less than 10000")
                else:
                    messagebox.showerror("Error","This much amount can not be inserted at a time (limit : 10000)")
        else:
            messagebox.showerror("Error","Enter the amount in even Order")
    else:
        messagebox.showerror("Error","Pin in Invalid")