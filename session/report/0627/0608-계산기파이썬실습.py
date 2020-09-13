from tkinter import *

def add():
    su1 = int(number01.get())
    su2 = int(number02.get())
    result["text"] = su1 + su2

def sub():
    su1 = int(number01.get())
    su2 = int(number02.get())
    result["text"] = su1 - su2

def mul():
    su1 = int(number01.get())
    su2 = int(number02.get())
    result["text"] = su1*su2

def div():
    su1 = int(number01.get())
    su2 = int(number02.get())

    result["text"] = su1/su2

calc = Tk()
calc.title("Calculator")
calc.geometry("160x100")

Label(calc, text="수-1").grid(row=0)
Label(calc, text="수-2").grid(row=1)
Label(calc, text="결과").grid(row=2)

number01 = Entry(calc, width=20)
number01.grid(row=0, column=1)
number02 = Entry(calc, width=20)
number02.grid(row=1, column=1)

result=Label(calc, relief='raised', width=17, bd=2, bg='green')
result.grid(row=2, column=1)

Button(calc, text='+', width=2, command= add).place(x=30, y=70)
Button(calc, text='-', width=2, command= sub).place(x=60, y=70)
Button(calc, text='*', width=2, command= mul).place(x=90, y=70)
Button(calc, text='/', width=2, command= div).place(x=120, y=70)

calc.mainloop()