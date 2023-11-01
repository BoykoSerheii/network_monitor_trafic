from tkinter import *
from tkinter import  ttk
import psutil

root = Tk()
max_num = [0, 0]

root['bg'] = '#fafafa'
root.title('Monitor network')
root.geometry('800x450')

root.resizable()
root.resizable(width=False, height=False)

canvas = Canvas(root)
canvas.pack(side=LEFT, fill=Y)

title = Label(canvas, text="Доступні мережі:", bg="#fafafa", font=40)
title.pack()

graf = Canvas(root, bg='red', width=560, height=300)
graf.pack(anchor=NE)

for nic, addrs in psutil.net_if_addrs().items():
    btn = ttk.Button(canvas, text="%s:" % (nic))
    btn.pack(fill=X, ipadx=10, ipady=10)

root.mainloop()
