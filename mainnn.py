from tkinter import *

root = Tk()
max_num = [0, 0]

root['bg'] = '#fafafa'
root.title('Monitor network')
root.geometry('600x450')

root.resizable()
#root.resizable(width=False, height=False)

canvas = Canvas(root, width=600, height=450)
canvas.pack(side=LEFT, fill=Y)

title = Label(canvas, text="text", bg="#fafafa", font=40)
title.pack()
entry = Entry(canvas)
entry.pack()
pas = Spinbox(canvas)
pas.pack()

root.mainloop()
