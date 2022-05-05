#Gui-mouse.py
from calendar import Calendar
import imp
from tkinter import * # Lib: Tk interface
from tkinter import ttk

import pyautogui as pg # ชื่อสำหรับเรียกใช้ 
import  webbrowser

GUI = Tk()
GUI.title('โปรแกรมสั่งกดปฏิทิน')
GUI.geometry('1000x300')

def calendar():
	pg.click(1777,1055)

B1 = Button(GUI,text='Calendar1', command=calendar)
B1.pack(ipadx=20, ipady=10, pady=20)

B2 = ttk.Button(GUI,text='Calendar2', command=calendar)
B2.pack(ipadx=20, ipady=10, pady=20)

def Google():
	webbrowser.open('http://www.google.com')

B3 = ttk.Button(GUI,text='Google', command=Google)
B3.pack(ipadx=20, ipady=10)

GUI.mainloop()