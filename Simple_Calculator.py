from tkinter import *

win = Tk()
win.title("Simple Calculator")

e = Entry(win, width = 35, borderwidth = 5)
e.grid(row=0, column=0, columnspan=3, padx=20,pady=10)

#e.insert(0, "Enter Your Name")

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clearing():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equals():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

#Define Buttons
button_1 = Button(win, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(win, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(win, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(win, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(win, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(win, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(win, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(win, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(win, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(win, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_addition = Button(win, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(win, text="=", padx=91, pady=20, command=button_equals)
button_clear = Button(win, text="Clear", padx=79, pady=20, command=button_clearing)

button_subtraction = Button(win, text="-", padx=41, pady=20, command=button_subtract)
button_multiplication = Button(win, text="*", padx=40, pady=20, command=button_multiply)
button_division = Button(win, text="/", padx=40, pady=20, command=button_divide)


#put the buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1, columnspan=2)
button_addition.grid(row=5,column=0)
button_equal.grid(row=5,column=1, columnspan=2)

button_subtraction.grid(row=6, column=0)
button_multiplication.grid(row=6, column=1)
button_division.grid(row=6, column=2)

win.mainloop()