#Session 41
#Make a Grade calculator as HW
from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.geometry("490x200")
root.config(bg="light blue")

operator=""
text_input=StringVar()
textDisplay=Entry(root,font=("arial",20,"bold"),textvariable=text_input,bd=30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)

def click(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def clear():
    global operator
    operator=""
    text_input.set("")

def equals():
    global operator
    sumup=str(eval(operator))  
    text_input.set(sumup)
    operator=""


b1=Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",15,"bold"),bg="cadet blue",text="1",command=lambda:click(1)).grid(row=3,column=0)



root.mainloop()
