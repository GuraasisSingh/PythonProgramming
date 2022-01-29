#Make a Grade calculator

from tkinter import *
root=Tk()
root.title("GRADE CALCULATOR")
root.geometry("500x450")    
root.config(bg="green3")

def Calculate():
    m=int(marks.get())
    if m>=90 and m<=100:
        grade="A"        
    elif m>=80 and m<=90 :
        grade="B"
    elif m>=70 and m<=80:
        grade="C"
    elif m>=60 and m<=70:
        grade="D"
    elif m>=50 and m<=60:
        grade="E"
    elif m>=0 and m<=50:
        grade="F"
    else:
        grade="Invalid"
    print=Label(text=f"Your Grade is {grade}",font="verdana 13 bold",bg="yellow",fg="blue")
    print.place(x=120,y=250)

def clear():
    marks.delete(0, END)
    
def exit():
    root.destroy()

enGrade=Label(root,text="Enter your Marks:",font="verdana 13 bold",bg="yellow",fg="blue")
enGrade.place(x=40, y=40)

mv=StringVar()
marks=Entry(root,font="verdana 13 bold",textvar=mv,width=8,bg="white",fg="black")
marks.place(x=250,y=40)

cal=Button(root,text="Calculate",font="verdana 13 bold",bg="yellow",fg="blue",command=Calculate)
cal.place(x=40,y=130)

Exit=Button(root,text="Exit",font=("verdana",13,"bold"),bg="yellow",fg="blue",command=exit)
Exit.place(x=270, y=130)

clear=Button(root,text="Clear",font=("verdana",13,"bold"),bg="yellow",fg="blue",command=clear)
clear.place(x=175, y=130)

root.mainloop()   
