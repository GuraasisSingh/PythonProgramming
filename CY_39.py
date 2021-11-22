'''
from tkinter import *
root=Tk()
root.title()
root.title("CI Calculator")
root.geometry("500x500")
root.config(bg="gold")
def Calculate():
    pg=int(pe.get())
    rg=int(re.get())
    tg=int(te.get())
    ci=(pg*((1+(rg/100))**tg))-pg
    Label(text=f"{ci}",font="arial 10").place(x=100,y=160)

p=Label(root,text="PRINCIPLE: ",font="arial 10",bg="green",fg="white").place(x=60,y=10)
r=Label(root,text="RATE: ",font="arial 10",bg="green",fg="white").place(x=60,y=30)
t=Label(root,text="TIME: ",font="arial 10",bg="green",fg="white").place(x=60,y=50)

pv=StringVar()
rv=StringVar()
tv=StringVar()

pe=Entry(root,font="arial 10",textvar=pv,width=8,bg="white",fg="black")
re=Entry(root,font="arial 10",textvar=rv,width=8,bg="white",fg="black")
te=Entry(root,font="arial 10",textvar=tv,width=8,bg="white",fg="black")

pe.place(x=140, y=10)
re.place(x=140, y=30)
te.place(x=140, y=50)

Button(root,text="Calculation",font="arial 10",bg="blue", fg="white",command=Calculate).place(x=100,y=90)
Button(root,text="Exit",font="arial 10",bg="blue", fg="white",command=lambda:exit()).place(x=200,y=90)


root.mainloop()
'''
from tkinter import *
import calendar
root=Tk()
root.geometry("500x550")
root.title("CALENDAR")
root.config(bg="limegreen")

def show():
    m=int(month.get())
    y=int(year.get())
    o=calendar.month(y,m)
    cal.insert("end",o)

def clear():
    cal.delete('1.0', END)

def exit():
    root.destroy()

m_label=Label(root,text="Month",font=("verdana","10","bold"))
m_label.place(x=20,y=50)

month=Spinbox(root,from_=1,to=12,width="2")
month.place(x=80,y=50)

y_label=Label(root,text="Year",font=("verdana","10","bold"))
y_label.place(x=120,y=50)

year=Spinbox(root,from_=1800,to=3000,width="5")
year.place(x=170,y=50)

cal=Text(root,width=21,height=6,borderwidth=2)
cal.place(x=50, y=110)

show=Button(root,text="Show",font=("verdana",8,"bold"),command=show)
show.place(x=20, y=250)

Exit=Button(root,text="Exit",font=("verdana",8,"bold"),command=exit)
Exit.place(x=170, y=250)


clear=Button(root,text="Clear",font=("verdana",8,"bold"),command=clear)
clear.place(x=100, y=250)

root.mainloop()

    




    
