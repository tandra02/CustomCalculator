import customtkinter
from tkinter import *

window = customtkinter.CTk()
window.title("CALCULATOR")
window.geometry("443x250")
window.config(bg="black")

index = 0
answer = ""
font1=("Arial",20,'bold')

def typeAnswer(value):
    global index
    global answer
    answer += value
    hello_entry.insert(index, value)
    index += 1
def per():
    global index
    global answer
    try:
        value = float(answer)
        value = (value / 100) * 100
        hello_entry.delete(0, "end")
        hello_entry.insert(0, value)
        answer = str(value)
        index = len(answer)
    except ValueError:
        hello_entry.delete(0, "end")
        hello_entry.insert(0, "Error")
        answer = ""
def clear():
    global index
    global answer
    hello_entry.delete(0,"end")
    answer = ""
    index = 0
def cal():
    global answer
    result = ""
    result = eval(answer)
    clear()
    hello_entry.insert(0, result)

title_label= customtkinter.CTkLabel(window,font=font1, text="Calculator",text_color="#6B8E23")
hello_entry = customtkinter.CTkEntry(window, width=250, font=font1, fg_color="#8FBC8F", border_color="#1e2b04", text_color="black")
hello_entry.grid(row=0, column=1, columnspan=2)  # Stretch the entry widget

clean = customtkinter.CTkButton(window, text="C",font=font1, width=50, height=4, command=clear, fg_color="#6B8E23", hover_color="#1e2b04")
clean.grid(row=1, column=0, sticky="ew", padx=2, pady=2, columnspan=2)  # Stretch the "C" button

percentage = customtkinter.CTkButton(window, command=lambda: per(), text="%",font=font1, width=150, height=4, fg_color="#6B8E23", hover_color="#1e2b04")
percentage.grid(row=1, column=2,padx=2,pady=2)
substract = customtkinter.CTkButton(window, text="/",font=font1,width=50,height=4, command=lambda: typeAnswer("/"),fg_color="#6B8E23",hover_color="#1e2b04")
substract.grid(row=1,column=3, padx=2,pady=2,sticky="ew",columnspan=1)
seven = customtkinter.CTkButton(window, text="7",font=font1,width=90,height=4, command=lambda: typeAnswer("7"),fg_color="#014421",hover_color="#1e2b04")
seven.grid(row=2,column=0,padx=2,pady=2,sticky="ew",columnspan=1)
eight = customtkinter.CTkButton(window, text="8",font=font1,width=90,height=4, command=lambda: typeAnswer("8"),fg_color="#014421",hover_color="#1e2b04")
eight.grid(row=2,column=1,padx=2,pady=2,sticky="ew",columnspan=1)
nine = customtkinter.CTkButton(window, text="9",font=font1,width=90,height=4, command=lambda: typeAnswer("9"),fg_color="#014421",hover_color="#1e2b04")
nine.grid(row=2,column=2,padx=2,pady=2,sticky="ew",columnspan=1)
plus = customtkinter.CTkButton(window, text="+",font=font1,width=90,height=4, command=lambda: typeAnswer("+"),fg_color="#6B8E23",hover_color="#1e2b04")
plus.grid(row=2,column=3,padx=2,pady=2,sticky="ew",columnspan=1)
four = customtkinter.CTkButton(window, text="4",font=font1,width=90,height=4, command=lambda: typeAnswer("4"),fg_color="#014421",hover_color="#1e2b04")
four.grid(row=3,column=0,padx=2,pady=2,sticky="ew",columnspan=1)
five = customtkinter.CTkButton(window, text="5",font=font1,width=90,height=4, command=lambda: typeAnswer("5"),fg_color="#014421",hover_color="#1e2b04")
five.grid(row=3,column=1,padx=2,pady=2,sticky="ew",columnspan=1)
six = customtkinter.CTkButton(window, text="6",font=font1,width=90,height=4, command=lambda: typeAnswer("6"),fg_color="#014421",hover_color="#1e2b04")
six.grid(row=3,column=2,padx=2,pady=2,sticky="ew",columnspan=1)
minus = customtkinter.CTkButton(window, text="-",font=font1,width=90,height=4, command=lambda: typeAnswer("-"),fg_color="#6B8E23",hover_color="#1e2b04")
minus.grid(row=3,column=3,padx=2,pady=2,sticky="ew",columnspan=1)
one = customtkinter.CTkButton(window, text="1",font=font1,width=90,height=4, command=lambda: typeAnswer("1"),fg_color="#014421",hover_color="#1e2b04")
one.grid(row=4, column=0,padx=2,pady=2,sticky="ew",columnspan=1)
two = customtkinter.CTkButton(window, text="2",font=font1,width=90,height=4, command=lambda: typeAnswer("2"),fg_color="#014421",hover_color="#1e2b04")
two.grid(row=4, column=1,padx=2,pady=2,sticky="ew",columnspan=1)
three = customtkinter.CTkButton(window, text="3",font=font1,width=90,height=4, command=lambda: typeAnswer("3"),fg_color="#014421",hover_color="#1e2b04")
three.grid(row=4,column=2,padx=2,pady=2,sticky="ew",columnspan=1)
multiply = customtkinter.CTkButton(window, text="*",font=font1,width=90,height=4, command=lambda: typeAnswer("*"),fg_color="#6B8E23",hover_color="#1e2b04")
multiply.grid(row=4,column=3,padx=2,pady=2,sticky="ew",columnspan=1)
zero = customtkinter.CTkButton(window, text="0",font=font1,width=90,height=4, command=lambda: typeAnswer("0"),fg_color="#014421",hover_color="#1e2b04")
zero.grid(row=5,column=0,sticky="ew",padx=2,pady=2,columnspan=2)
equal = customtkinter.CTkButton(window, text="=",font=font1,width=150, height=4, command=lambda: cal(), fg_color="#2f522f", hover_color="#1e2b04")
equal.grid(row=5, column=2,sticky="ew",padx=4,pady=4, columnspan=5)  # Stretch the "=" button

window.mainloop()