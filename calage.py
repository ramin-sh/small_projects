from tkinter import *
from datetime import date

root=Tk()
root.geometry('300x300')
root.title("حسابگر سن")

def CalAge():
    today=date.today()
    birthDate=date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age=today.year - birthDate.year -((today.month, today.day) < (birthDate.month,birthDate.day))
    Label(text=f"{nameValue.get()} your age is {age}").grid(row=6, column=1)
    

Label(text=":نام").grid(row=1, column=1, padx=90)
Label(text=":سال").grid(row=2, column=1)
Label(text=":ماه").grid(row=3, column=1)
Label(text=":روز").grid(row=4, column=1)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()
nameEntry = Entry(root,textvariable=nameValue)
yearEntry = Entry(root,textvariable=yearValue)
monthEntry = Entry(root,textvariable=monthValue)
dayEntry = Entry(root,textvariable=dayValue)
nameEntry .grid(row=1 ,column=0, pady=10)
yearEntry.grid(row=2 ,column=0, pady=10)
monthEntry.grid(row=3 ,column=0, pady=10)
dayEntry.grid(row=4 ,column=0, pady=10)

Button(text="حساب کردن سن",command=CalAge,).grid(row=5,column=0,pady=10)
root.mainloop() 

