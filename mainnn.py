from tkinter import *
from tkinter import  ttk

root = Tk()
max_num = [0, 0]

root['bg'] = '#fafafa'
root.title('Monitor network')
root.geometry('600x450')

root.resizable()
#root.resizable(width=False, height=False)

canvas = Canvas(root, width=600, height=450)
canvas.pack(side=LEFT, fill=Y)

title = Label(canvas, text="Доступні мережі:", bg="#fafafa", font=40)
title.pack()

for r in range(3):
    for c in range(3):
        btn = ttk.Button(canvas, text=f"({r},{c})")
        btn.pack()

root.mainloop()
