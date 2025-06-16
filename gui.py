"""from tkinter import*
win=Tk()
win.title("hello")
win.geometry('400x200')
label=Label(win,text="Hello, Students!",font=("Arial Bold",30))
label.config(bg='red',fg='white')
label.pack(side = "left",pady=150, ipady=50)
win.mainloop()

#window
from tkinter import*
win=Tk()
win.title("hello")
win.geometry('400x200')

def button_clicked():
    print("Button clicked!")

button=Button(win,text="hello,students",command=button_clicked)
button.pack(padx=20,pady=20)

win.mainloop()

#change button text on click
from tkinter import*
win=Tk()
win.title("hello")
win.geometry('400x200')

def button_clicked():
    button.config(text="Good job",bg="red",fg="white")

button=Button(win,text="hello,students",command=button_clicked)
button.pack(padx=20,pady=20)

win.mainloop()

#numeric widgets
from tkinter import*
win=Tk()
win.title("scale example")
win.geometry('300x100')

#create scale widget
scale=Scale(win,from_=0, to=100, orient=HORIZONTAL)
scale.pack()
win.mainloop()

#spinbox widget
from tkinter import*
win=Tk()
win.title("spinbox example")
win.geometry('300x100')

#create scale widget
spinbox=Spinbox(win,from_=0, to=10)
spinbox.pack()
win.mainloop()

#boolean widget
# most common = checkbutton, radiobutton
#check button
from tkinter import*
from tkinter import Radiobutton

win=Tk()
win.title("checkbutton example")
win.geometry('300x100')

check_var=BooleanVar()
checkbutton=Checkbutton(win,text="check me",variable=check_var)
checkbutton.pack()
win.mainloop()

#radio button
from tkinter import*
win=Tk()
win.title("radiobutton example")
win.geometry('300x100')

radio_var=StringVar()
radiobutton1=Radiobutton(win,text="Male",variable=radio_var,value="male")
radiobutton2=Radiobutton(win,text="female",variable=radio_var,value="female")

radiobutton1.pack()
radiobutton2.pack()
win.mainloop()

#listbox
from tkinter import*
win=Tk()
win.title("radiobutton example")
win.geometry('300x100')

#create listbox
listbox=Listbox(win)
listbox.insert(1,"option1")
listbox.insert(2,"option2")
listbox.insert(3,"option3")
listbox.insert(4,"option4")
listbox.insert(5,"option5")
listbox.pack()
win.mainloop()

#combobox
import tkinter as tk
from tkinter.ttk import Combobox

window = tk.Tk()
window.title("Combobox Example")
window.geometry('800x200')

def combobox_selected(event):
    selected_value = combobox.get()
    label.config(text=f"Selected: {selected_value}")

# Create a label to display selected value
label = tk.Label(window, text="Select an option:")
label.pack(padx=20, pady=10)

# Create a combobox widget
options = ["option1", "option2", "option3"]
combobox = Combobox(window, values=options)
combobox.pack(padx=20, pady=10)

# Bind combobox selection event to handler
combobox.bind("<<ComboboxSelected>>", combobox_selected)

window.mainloop()


#entry widget
from tkinter import*
win=Tk()
win.title("entry example")
win.geometry('300x100')

#entry widget -->
entry=Entry(win)
entry.pack()
win.mainloop()

#create login page using grid
from tkinter import *

win = Tk()
win.title("Login Example")
win.geometry('300x150')

def submit_clicked():
    result_label.config(text="Good job!")

# Username
username_label = Label(win, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)

username_entry = Entry(win)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password
password_label = Label(win, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)

password_entry = Entry(win, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Submit Button
submit_button = Button(win, text="Submit", command=submit_clicked)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
result_label = Label(win, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

win.mainloop()

from tkinter import*
from tkcalendar import DateEntry

root=Tk()
root.title("Daate picker example")
root.geometry('800x200')

#create widget
date_entry = DateEntry(root)
date_entry.pack()
root.mainloop()

#color picker
from tkinter import*
from tkinter import colorchooser

def choose_color():
    color_code=colorchooser.askcolor(title="choose a color")
    print(color_code)

root=Tk()
root.title("Color picker example")
root.geometry('800x200')

#create button
button=Button(root,text="choose color",command=choose_color)
button.pack()
root.mainloop()

#canvas example
import tkinter as tk
root=tk.Tk()
root.title("canvas example")

canvas=tk.Canvas(root,width=400,height=300)
canvas.pack()

canvas.create_line(0,0,200,100)
canvas.create_rectangle(50,50,150,150,fill="blue")
root.mainloop()"""

#sum calculator
from tkinter import*

win = Tk()
win.title("sum calculator")
win.geometry('800x200')

def calculate_sum():
    num1=float(entry1.get())
    num2=float(entry2.get())
    total=num1+num2
    result_label.config(text=f"sum: {total}")
# num1
label1 = Label(win, text="number1:")
label1.grid(row=0, column=0, padx=10, pady=5)

entry1 = Entry(win)
entry1.grid(row=0, column=1, padx=10, pady=5)

#num2
label2 = Label(win, text="number2:")
label2.grid(row=1, column=0, padx=10, pady=5)

entry2 = Entry(win)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Submit Button
submit_button = Button(win, text="Calculate sum", command=calculate_sum)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
result_label = Label(win, text="Sum: ")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

win.mainloop()