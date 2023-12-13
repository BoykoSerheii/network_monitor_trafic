from tkinter import *
import psutil
import time
from psutil._common import bytes2human
import threading

root = Tk()
max_num = [0, 0]
start_trafic = list(psutil.net_io_counters())

def f():
  threading.Timer(1, f).start()  # Перезапуск через 5 секунд
  btn_click()

def clear():
    max_num[0] = 0
    max_num[1] = 0
    num = list(psutil.net_io_counters())
    start_trafic[0] = num[0]
    start_trafic[1] = num[1]

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
    title['text'] = f"out trafic: {bytes2human(aft[0]-bef[0])}/s."
    title1['text'] = f"input trafic: {bytes2human(aft[1]-bef[1])}/s."
    title2['text'] = f"max out trafic: {bytes2human(max_num[0])}/s."
    title3['text'] = f"max input trafic: {bytes2human(max_num[1])}/s."
    title4['text'] = f"total out trafic: {bytes2human(bef[0]-(start_trafic[0]*8))}/s."
    title5['text'] = f"total input trafic: {bytes2human(bef[1]-(start_trafic[1]*8))}/s."




def poll(interval):
    """Необработанная статистика в интервале `interval`."""
    pnic_before = psutil.net_io_counters()
    # спим в течении `interval`
    time.sleep(interval)
    pnic_after = psutil.net_io_counters()
    return (pnic_before, pnic_after)

root['bg'] = '#fafafa'
root.title('Monitor network')
#root.wm_attributes('-alpha', 0.9)
root.geometry('300x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250, bg="#fafafa")
canvas.pack()

#frame = Frame(root, bg='orange')
#frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(canvas, text="out trafic: 0", bg="#fafafa", font=40)
title.pack()
title1 = Label(canvas, text="input trafic: 0", bg="#fafafa", font=40)
title1.pack()
title2 = Label(canvas, bg="#fafafa", font=40)
title2.pack()
title3 = Label(canvas, bg="#fafafa", font=40)
title3.pack()
title4 = Label(canvas, bg="#fafafa", font=40)
title4.pack()
title5 = Label(canvas, bg="#fafafa", font=40)
title5.pack()
button = Button(canvas, bg="green", text="Clear", command=clear)
button.pack()

f()
root.mainloop()
