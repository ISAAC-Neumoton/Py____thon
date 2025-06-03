from tkinter import *

# define the root window
root = Tk()
# set the title of the window
root.title("Calculator")
root.geometry("400x600")
input = Entry(root, width= 30, font=("Arial", 16), borderwidth=2, relief="groove",)

# displaay the input field
input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def click(number):
    # input.delete(0, END)
    num = input.get()
    input.delete(0, END)
    input.insert(0, num + number)

def add():
    num_1 = input.get()
    global num1
    num1 = int(num_1)
    input.delete(0, END)
    
def equal():
    num_2 = input.get()
    input.delete(0, END)
    input.insert(0, int(num_2) + num1)
    


# buttons for digits and operations
btn_1 = Button(root, text="1", width=6, height=2, font = ("Arial", 16), command=lambda: click("1"))
btn_2 = Button(root, text="2", width=6, height=2, font=("Arial", 16), command=lambda: click("2"))
btn_3 = Button(root, text="3", width=6, height=2, font=("Arial", 16), command=lambda: click("3"))
btn_4 = Button(root, text="4", width=6, height=2, font=("Arial", 16), command=lambda: click("4"))
btn_5 = Button(root, text="5", width=6, height=2, font=("Arial", 16), command=lambda: click("5"))
btn_6 = Button(root, text="6", width=6, height=2, font=("Arial", 16), command=lambda: click("6"))
btn_7 = Button(root, text="7", width=6, height=2, font=("Arial", 16), command=lambda: click("7"))
btn_8 = Button(root, text="8", width=6, height=2, font=("Arial", 16), command=lambda: click("8"))
btn_9 = Button(root, text="9", width=6, height=2, font=("Arial", 16), command=lambda: click("9"))
btn_0 = Button(root, text="0", width=6, height=2, font=("Arial", 16), command=lambda: click("0"))
btn_add = Button(root, text="+", width=6, height=2, font=("Arial", 16), command= add)
btn_dot = Button(root, text=".", width=6, height=2, font=("Arial", 16), command=lambda: click())
btn_equal = Button(root, text="=", width=17, height=2, font=("Arial", 16), command=equal)
btn_clear = Button(root, text="Clear", width=6, height=2, font=("Arial", 16), command=lambda: input.delete(0, END) )

btn_9.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_7.grid(row=1, column=2)

btn_6.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_4.grid(row=2, column=2)

btn_3.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_1.grid(row=3, column=2)
btn_0.grid(row=4, column=0)
btn_dot.grid(row=5, column=0)

btn_add.grid(row=4, column=1)
btn_equal.grid(row=5, column=1, columnspan=2)
btn_clear.grid(row=4, column=2,)



mainloop()