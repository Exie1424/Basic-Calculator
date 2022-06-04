## Basic Calculator
import math
from tkinter import *

# Creating a window
window = Tk()
window.title("Calculator")

# User input
userInput = Entry(window,width= 45, borderwidth=10)
userInput.grid(row=0, column=0, columnspan=3)

# Button Functionality 

def buttonClicked(number):
    currentNum = userInput.get()
    userInput.delete(0, END)
    userInput.insert(0, str(currentNum) + str(number))

def buttonAdd():
    firstNumber = userInput.get()
    global firstNum
    global math
    firstNum = int(firstNumber)
    math = "Add"
    userInput.delete(0, END)

def buttonSub():
    firstNumber = userInput.get()
    global firstNum
    global math
    firstNum = int(firstNumber)
    math = "Subtract"
    userInput.delete(0, END)
    
def buttonMultiply():
    firstNumber = userInput.get()
    global firstNum
    global math
    firstNum = int(firstNumber)
    math = "Multiply"
    userInput.delete(0, END)

def buttonDivide():
    firstNumber = userInput.get()
    global firstNum
    global math
    firstNum = int(firstNumber)
    math = "Divide"
    userInput.delete(0, END)
    
def buttonPercentage():
    firstNumber = userInput.get()
    global firstNum
    global math
    firstNum = int(firstNumber)
    math = "Percentage"
    userInput.delete(0, END)

def buttonClear():
    userInput.delete(0, END)
    
def buttonEquals():
    secondNumber = userInput.get()
    userInput.delete(0, END)

    # Executing correct function
    if math == "Add":
        userInput.insert(0, firstNum + int(secondNumber))
    elif math == "Subtract":
        userInput.insert(0, firstNum - int(secondNumber))
    elif math == "Multiply":
        userInput.insert(0, firstNum * int(secondNumber))
    elif math == "Divide":
        userInput.insert(0, firstNum / int(secondNumber))
    elif math == "Percentage":
        userInput.insert(0, (firstNum/100)* int(secondNumber))


## Button Formatting
# Number Buttons
button1 = Button(window, text="1", padx= 40, pady= 25, command=lambda: buttonClicked(1)).grid(row=4, column=0)
button2 = Button(window, text="2", padx= 40, pady= 25, command=lambda: buttonClicked(2)).grid(row=4, column=1)
button3 = Button(window, text="3", padx= 40, pady= 25, command=lambda: buttonClicked(3)).grid(row=4, column=2)

button4 = Button(window, text="4", padx= 40, pady= 25, command=lambda: buttonClicked(4)).grid(row=3, column=0)
button5 = Button(window, text="5", padx= 40, pady= 25, command=lambda: buttonClicked(5)).grid(row=3, column=1)
button6 = Button(window, text="6", padx= 40, pady= 25, command=lambda: buttonClicked(6)).grid(row=3, column=2)

button7 = Button(window, text="7", padx= 40, pady= 25, command=lambda: buttonClicked(7)).grid(row=2, column=0)
button8 = Button(window, text="8", padx= 40, pady= 25, command=lambda: buttonClicked(8)).grid(row=2, column=1)
button9 = Button(window, text="9", padx= 40, pady= 25, command=lambda: buttonClicked(9)).grid(row=2, column=2)

button0 = Button(window, text="0", padx= 40, pady= 25, command=lambda: buttonClicked(0)).grid(row=5, column=1)

# Operational Buttons

buttonAdd = Button(window, text="+", padx=40, pady= 25, command=buttonAdd).grid(row=5, column=0)
buttonSub = Button(window, text="-", padx=40, pady= 25, command=buttonSub).grid(row=5, column=2)

buttonMultiply = Button(window, text="*", padx=40, pady= 25, command=buttonMultiply).grid(row=1, column=0)
buttonDivide = Button(window, text="/", padx=40, pady= 25, command=buttonDivide).grid(row=1, column=1)
buttonPercentage = Button(window, text="%", padx=40, pady= 25, command=buttonPercentage).grid(row=1, column=2)

buttonEquals = Button(window, text="=", padx=40, pady=25, command=buttonEquals).grid(row= 6, column=2)
buttonClear = Button(window, text="Clear", padx=80, pady=25, command=buttonClear).grid(row= 6, column=0, columnspan=2)



window.mainloop()