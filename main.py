from tkinter import *
expression = ""

root = Tk()
root.configure(background="deepskyblue4")
root.title("My calculator")
root.geometry("325x200")

mymath = StringVar()
mathbox = Entry(root,textvariable=mymath)
mathbox.grid(columnspan=5, ipadx=70)

def key_press(number):
    global expression
    expression = expression+ str(number)
    print(expression)
    mymath.set(expression)

def total():
    global expression
    total2 = str(eval(expression))
    mymath.set(total2)
    expression = ""

def clear():
    global expression
    expression = ""
    mymath.set("")

button1 = Button(root, text="1", fg="black", bg="ivory4", command = lambda: key_press(1), height=1, width=5)
button1.grid(row=3, column=1)

button2 = Button(root, text="2", fg="black", bg="ivory4", command = lambda: key_press(2), height=1, width=5)
button2.grid(row=3, column=2)

button3 = Button(root, text="3", fg="black", bg="ivory4", command = lambda: key_press(3), height=1, width=5)
button3.grid(row=3, column=3)

button4 = Button(root, text="4", fg="black", bg="ivory4", command = lambda: key_press(4), height=1, width=5)
button4.grid(row=2, column=1)

button5 = Button(root, text="5", fg="black", bg="ivory4", command = lambda: key_press(5), height=1, width=5)
button5.grid(row=2, column=2)

button6 = Button(root, text="6", fg="black", bg="ivory4", command = lambda: key_press(6), height=1, width=5)
button6.grid(row=2, column=3)

button7 = Button(root, text="7", fg="black", bg="ivory4", command = lambda: key_press(7), height=1, width=5)
button7.grid(row=1, column=1)

button8 = Button(root, text="8", fg="black", bg="ivory4", command = lambda: key_press(8), height=1, width=5)
button8.grid(row=1, column=2)

button9 = Button(root, text="9", fg="black", bg="ivory4", command = lambda: key_press(9), height=1, width=5)
button9.grid(row=1, column=3)

button0 = Button(root, text="0", fg="black", bg="ivory4", command = lambda: key_press(0), height=1, width=5)
button0.grid(row=4, column=2)

buttonequals =  Button(root, text="=", fg="black", bg="ivory4", command = lambda: total(), height=1, width=5)
buttonequals.grid(row=5, column=4)

buttonplus =  Button(root, text="+", fg="black", bg="ivory4", command = lambda: key_press("+"), height=1, width=5)
buttonplus.grid(row=4, column=4)

buttonminus = Button(root, text="-", fg="black", bg="ivory4", command = lambda: key_press("-"), height=1, width=5)
buttonminus.grid(row=3, column=4)

buttontimes = Button(root, text="*", fg="black", bg="ivory4", command = lambda: key_press("*"), height=1, width=5)
buttontimes.grid(row=2, column=4)

buttondivide = Button(root, text="/", fg="black", bg="ivory4", command = lambda: key_press("/"), height=1, width=5)
buttondivide.grid(row=1, column=4)

buttondot = Button(root, text=".", fg="black", bg="ivory4", command = lambda: key_press("."), height=1, width=5)
buttondot.grid(row=4, column=1)

buttonclear = Button(root, text="C", fg="black", bg="ivory4", command = clear, height=1, width=5)
buttonclear.grid(row=4, column=3)


root.mainloop()