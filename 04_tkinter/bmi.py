from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100
    bmi = weight / (height**2)

    bmi_label.config(text="ค่า BMI ของคุณคือ {:.2f}".format(bmi))

app = Tk()
app.title('คำนวณ BMI')
app.geometry('500x420')

img_bmi_logo = ImageTk.PhotoImage(Image.open("bmi-logo.png"))
ImageTk.PhotoImage(Image.open("bmi-logo.png").resize((200,200), Image.LANCZOS))
img_bmi = ImageTk.PhotoImage(Image.open("bmi.jpg"))
img_bmichart = ImageTk.PhotoImage(Image.open("bmi-chart.jpg"))


############ imag_bmi
frame_1 = Frame(app) #สร้างเฟรม
frame_1.place(x=40,y=20)
label_1 = Label(frame_1,image=img_bmi_logo)
label_1.pack()

############ img_bmichart
frame_2 = Frame(app) #สร้างเฟรม
frame_2.place(x=0,y=150)
label_2 = Label(frame_2,image=img_bmichart)
label_2.pack()

############
frame_3 = Frame(app) #สร้างเฟรม
frame_3.place(x=180,y=20)

weight_label = ttk.Label(frame_3, text="น้ำหนัก (กก.):")
weight_label.pack()

weight_entry = ttk.Entry(frame_3)
weight_entry.pack()

height_label = ttk.Label(frame_3, text="ความสูง(ซม.):")
height_label.pack()

height_entry = ttk.Entry(frame_3)
height_entry.pack()

calculate_button = ttk.Button(frame_3, text="คำนวณ BMI", command=calculate_bmi)
calculate_button.pack()

bmi_label = ttk.Label(frame_3, text="")
bmi_label.pack()

############

app.mainloop()






