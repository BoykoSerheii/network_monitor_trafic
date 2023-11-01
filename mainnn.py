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

canvas = Canvas(root, highlightcolor="#E8E8E8")
canvas.pack(side=LEFT, fill=Y)

title = Label(canvas, text="Доступні мережі:", bg="#fafafa", font=40)
title.pack()

graf = Canvas(root, bg='#E8E8E8', width=560, height=320)
graf.pack(anchor=NE)

for i in range(0, 280, 40):
    graf.create_line(0, i + 40, 560, i + 40, fill="#C7C7C7")
    print(i)

for i in range(0, 520, 40):
    graf.create_line(i + 40, 0, i + 40, 320, fill="#C7C7C7")
    print(i)

graf.create_rectangle(3, 3, 558, 318, outline="#6E6E6E", width=2)

for nic, addrs in psutil.net_if_addrs().items():
    btn = ttk.Button(canvas, text="%s:" % (nic))
    btn.pack(fill=X, ipadx=10, ipady=10)

root.mainloop()
