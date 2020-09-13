from tkinter import *
import random

def pandan():
    su = int(number.get())
    if(su==star):
        print('ok')
    else:
        print('not')

game = Tk()
game.title("How many stars?")

star = random.randint(1, 10)

for n in range(0, star):
    Label(game, text="*", bg='green', relief='sunken').place(x=n*20, y=10)

Label(game, text="몇 개 일까요?").place(x=0, y=30)

number = Entry(game, width=5)
number.place(x=80, y=30)
number.focus_set()

Button(game, text="확인", width=2, command=pandan).place(x=0, y=60)

game.mainloop()