from tkinter import *
from tkinter import ttk, messagebox
import psutil
import threading
import time
from psutil._common import bytes2human

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

title = Label(root, text="out trafic: 0", bg="#fafafa", font=40)
title.pack(anchor=W)
title1 = Label(root, text="input trafic: 0", bg="#fafafa", font=40)
title1.pack(anchor=W)
steps = []
mass = []
point = [0]
networkLine = []
status = [1]


def paint(canvas, size_cells, step, array_data):
    if len(steps) == 0:
        steps.append(size_cells)
    graf.delete(ALL)
    canvas_width = canvas.winfo_width()-2
    canvas_height = canvas.winfo_height()-4
    for i in range(0, canvas_height-size_cells, size_cells):                                                #Цикл для рисування горизонтальних ліній.
        graf.create_line(0, i + size_cells, canvas_width, i + size_cells, fill="#C7C7C7")

    for i in range(0, canvas_width, size_cells):                                                #Цикл для рисування вертикальних ліній.
        graf.create_line(i + steps[0], 0, i + steps[0], canvas_height, fill="#C7C7C7")

    x = [0, 1]
    for i in range(0, canvas_width, step):                                                #Цикл для рисування лінії даних.
        graf.create_line(i, (array_data[x[0]]-canvas_width)*(-1), i + step, (array_data[x[1]]-canvas_width)*(-1), fill="#D9180C")
        x[0] = x[0] + 1
        x[1] = x[1] + 1

    graf.create_rectangle(3, 3, canvas_width-1, canvas_height+1, outline="#6E6E6E", width=2)          #Рисування периметру графіка.

    if steps[0] != 0:
        steps[0] = steps[0] - step
    else:
        steps[0] = size_cells - step

def poll(interval):
    """Необработанная статистика в интервале `interval`."""
    pnic_before = psutil.net_io_counters(pernic=True)
    # спим в течении `interval`
    time.sleep(interval)
    pnic_after = psutil.net_io_counters(pernic=True)
    print(pnic_after)
    return (pnic_before[f'{networkLine[point[0]]}'], pnic_after[f'{networkLine[point[0]]}'])

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
    update(aft[0]-bef[0], mass[point[0]])
    title['text'] = f"out trafic: {bytes2human(aft[0] - bef[0])}/s."
    title1['text'] = f"input trafic: {bytes2human(aft[1] - bef[1])}/s."

def click_button(name):
    point[0] = networkLine.index(name)

def update(date,array_data):
    if len(array_data) == 0:
        for i in range(57):
            array_data.append(0)
    array_data.pop(0)
    array_data.append(date/100)
    print(mass)

for nic, addrs in psutil.net_if_addrs().items():                               #Додає кнопки згідно кількості мереж.
    btn = ttk.Button(canvas, text="%s:" % (nic), command=lambda nic=nic: click_button(nic))
    btn.pack(fill=X, ipadx=10, ipady=10)
    networkLine.append(nic)

for i in range(len(networkLine)):
        mass.append([])

def f():
    if status[0] == 1:
        threading.Timer(1, f).start()                                                #Перезапуск через 1 секунд
    else:
        status[0] = 0
    btn_click()
    size_cells = 20
    count = 10
    paint(graf, size_cells, count, mass[point[0]])

def on_closing():
    status[0] = 0
    root.destroy()

f()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()                                                                #Запуск вікна.
