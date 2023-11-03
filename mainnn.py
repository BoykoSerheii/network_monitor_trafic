from tkinter import *
from tkinter import ttk
import psutil
import threading
import time

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
mass = [0, 1, 60, 100, 20, 20, 580, 0, 20, 25, 40, 40, 60, 100, 10]
def paint():
    graf.delete(ALL)
    for i in range(0, 280, 40):                                                #Цикл для рисування горизонтальних ліній.
        graf.create_line(0, i + 40, 560, i + 40, fill="#C7C7C7")

    for i in range(0, 560, 40):                                                #Цикл для рисування горизонтальних ліній.
        graf.create_line(i + num[0], 0, i + num[0], 320, fill="#C7C7C7")

    x = [0, 1]
    for i in range(0, 560, 40):
        graf.create_line(i, mass[x[0]] + 40, i + 40, mass[x[1]] + 40, fill="#D9180C")
        x[0] = x[0] + 1
        x[1] = x[1] + 1

    graf.create_rectangle(3, 3, 559, 321, outline="#6E6E6E", width=2)          #Рисування периметру графіка.

    if num[0] != 40:
        num[0] = num[0] + 10
    else:
        num[0] = 10

def poll(interval):
    """Необработанная статистика в интервале `interval`."""
    pnic_before = psutil.net_io_counters()
    # спим в течении `interval`
    time.sleep(interval)
    pnic_after = psutil.net_io_counters()
    return (pnic_before, pnic_after)

max_num = [0, 0]
def btn_click():
    before, after = poll(1)
    bef = list(before)
    aft = list(after)
    bef[0] = bef[0] * 8
    bef[1] = bef[1] * 8
    aft[0] = aft[0] * 8
    aft[1] = aft[1] * 8
    if aft[0]-bef[0] > max_num[0]:
        max_num[0] = aft[0]-bef[0]
    if aft[1]-bef[1] > max_num[1]:
        max_num[1] = aft[1]-bef[1]
    update(aft[0]-bef[0])

def update(date):
    mass.pop(0)
    mass.append(date/100)

for nic, addrs in psutil.net_if_addrs().items():                               #Додає кнопки згідно кількості мереж.
    btn = ttk.Button(canvas, text="%s:" % (nic))
    btn.pack(fill=X, ipadx=10, ipady=10)

def f():
  threading.Timer(1, f).start()                                                #Перезапуск через 5 секунд
  btn_click()
  paint()

f()
root.mainloop()                                                                #Запуск вікна.
