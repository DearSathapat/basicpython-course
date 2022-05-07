
from cProfile import label
from cgi import test
from email.mime import image
from tkinter import * #เรียก interface ขึ้นมา
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk

GUI = Tk()
GUI.title('โปรแกรมคำนวณคาดการณ์เงินปันผลหุ้น A')
GUI.geometry('500x300') # กำหนดขนาดของโปรแกรม

#bg = PhotoImage(file='car.png')

#BG = Label(GUI, image=bg)
#BG = Pack()

image1 = image.open("C:\Users\Dear\Desktop\Basic Python\car.png")
test = ImageTk.PhotoImage(image1)

label1 =tkinter.Label(image=test)
label1.image = test
label1.place(x=x_)


L = Label(GUI,text='กรุณากรอกจำนวน', font=(None,20)) #กำหนดกล่องข้อความ
L.pack() # เอาตัว label ไปติดกับโปรแกรม

#def dear():

  #  DD = ttk.Button(GUI,text='คำนวณ', command=dear)
   # DD.pack(ipadx=20, ipady=10)

    

GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา