#Entry window
'''
from tkinter import *
root=Tk()
root.title("Entry Window")
root.geometry("500x450")
root.config(bg="cyan")
def Calculate():
   pass

ew=Label(root,text="Entry Window",font="verdana 20 bold",bg="white",fg="black")
ew.place(x=40,y=20)

a=Label(root,text="Admission number:",font="verdana 8 bold",bg="cyan",fg="black")
a.place(x=40,y=80)
n=Label(root,text="Number of Years:",font="verdana 8 bold",bg="red",fg="white")
n.place(x=40,y=100)
l=Label(root,text="Loan Amount:",font="verdana 8 bold",bg="red",fg="white")
l.place(x=40,y=120)

av=StringVar()
nv=StringVar()
lv=StringVar()

ae=Entry(root, font="verdana 8 bold",textvar=av,width=8,fg="black",bg="white")
ne=Entry(root, font="verdana 8 bold",textvar=nv,width=8,fg="black",bg="white")
le=Entry(root, font="verdana 8 bold",textvar=lv,width=8,fg="black",bg="white")

ae.place(x=180,y=80)
ne.place(x=180,y=100)
le.place(x=180, y=120)

b=Button(root, text="Insert",font="arial 8",bg="red", fg="white",command=Calculate)
b.place(x=180,y=180)

root.mainloop()
'''