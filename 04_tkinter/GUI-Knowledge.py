from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()#หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Sarabun',16),fg='green')
L1.place(x=20,y=30)

##################
def Button1():
    text = 'Python-101'
    messagebox.showinfo('วิชาเรียน',text)

FB1 = Frame(GUI) #สร้างเฟรม
FB1.place(x=100,y=80)
B1 = ttk.Button(FB1,text='วิชาเรียน',command=Button1)
B1.pack(ipadx=10,ipady=10)
##################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) #สร้างเฟรม
FB1.place(x=100,y=230)
B2 = ttk.Button(FB1,text='แสดงยอดเงิน',command=Button2)
B2.pack(ipadx=10,ipady=10)
##################

GUI.mainloop()
