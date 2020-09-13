from tkinter import *

def neon():
    text = NeonEntry.get()
    size = len(NeonEntry.get())
    NeonEntry.delete(0)
    NeonEntry.insert(size-1, text[0])

parent = Tk()

NeonEntry = Entry(parent)

NeonEntry.grid(row=0, column=1)
NeonEntry.focus_set()

Button(parent, text='Neon', command=neon).grid(row=1, column=1)

mainloop()

# -----------------------------------------------

