#! python3

from tkinter import Tk, Button, Entry, END
from time import sleep, ctime
from threading import Thread
from random import random


def tick():
    date.delete(0, END)
    date.insert(0, ctime())
    if shared:
        out.delete(0, END)
        out.insert(0, shared.pop())
    root.after(500, tick)


def heavy_computation():
    sleep(3)
    shared.append(random())

shared = []

root = Tk()
date = Entry(root)
date.pack()
out = Entry(root)
out.pack()
push = Button(root, text='start heavy process',
              command=lambda: Thread(target=heavy_computation).start())
push.pack()

tick()
