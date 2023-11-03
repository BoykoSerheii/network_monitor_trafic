from tkinter import *
from tkinter import ttk
import psutil
import threading

root = Tk()                                                                    #Створення вікна.

root['bg'] = '#fafafa'                                                         #Колір фону вікна.
root.title('Monitor network')                                                  #Створено назву вікна.
root.geometry('800x450')                                                       #Задано розмірі вікна.

root.resizable(width=False, height=False)                                      #Блокування зміни розміру вікна користувчем.

canvas = Canvas(root, highlightcolor="#E8E8E8")                                #Створення поля для рисування.
canvas.pack(side=LEFT, fill=Y)                                                 #Відображення з лівої сторони та по всій висоті.

title = Label(canvas, text="Доступні мережі:", bg="#fafafa", font=40)          #Створення поля для тексту.
title.pack()

graf = Canvas(root, bg='#E8E8E8', width=560, height=320)                       #Створення поля для рисування графіка.
graf.pack(anchor=NE)                                                           #Відображення від верхнього правого кута.

num = [0]
def paint():
    graf.delete(ALL)
    for i in range(0, 280, 40):                                                #Цикл для рисування горизонтальних ліній.
        graf.create_line(0, i + 40, 560, i + 40, fill="#C7C7C7")
    for i in range(0, 560, 40):                                                #Цикл для рисування горизонтальних ліній.
        graf.create_line(i + num[0], 0, i + num[0], 320, fill="#C7C7C7")
    graf.create_rectangle(3, 3, 558, 318, outline="#6E6E6E", width=2)          #Рисування периметру графіка.
    if num[0] != 40:
        num[0] = num[0] + 10
    else:
        num[0] = 10

for nic, addrs in psutil.net_if_addrs().items():                               #Додає кнопки згідно кількості мереж.
    btn = ttk.Button(canvas, text="%s:" % (nic))
    btn.pack(fill=X, ipadx=10, ipady=10)

def f():
  threading.Timer(1, f).start()  # Перезапуск через 5 секунд
  paint()

f()
root.mainloop()                                                                #Запуск вікна.
