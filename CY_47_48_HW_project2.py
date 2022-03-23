#Weather App
from tkinter import *
root=Tk()
root.title("Weather App")
root.geometry("800x850")
root.config(bg="white")
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
frame=Frame(root)
frame.pack(side=TOP)

def Calculate(): 
    city=entName.get()   
    if city=="Noida":
        g=Label(bottomframe,text="19℃\tMostly Sunny\n\tNoida,Uttar Pradesh",fg="WHITE",bg="Black",width=30,height=6,font="verdana 15 bold")
        g.pack(side=LEFT)
        h=Label(bottomframe,text="Friday\n3:00 PM",fg="Black",bg="cyan",width=30,height=6,font="verdana 15 bold")
        h.pack(side=RIGHT)
    elif city=="Chandigarh":
        g=Label(bottomframe,text="25℃\tMostly Sunny\n\tChandigarh,Punjab",fg="WHITE",bg="Black",width=30,height=6,font="verdana 15 bold")
        g.pack(side=LEFT)
        h=Label(bottomframe,text="Saturday\n7:00 PM",fg="Black",bg="cyan",width=30,height=6,font="verdana 15 bold")
        h.pack(side=RIGHT)
    elif city=="Mumbai":
        g=Label(bottomframe,text="20℃\tRainy\n\tMumbai,Maharashtra",fg="WHITE",bg="Black",width=30,height=6,font="verdana 15 bold")
        g.pack(side=LEFT)
        h=Label(bottomframe,text="Monday\n10:00 AM",fg="Black",bg="cyan",width=30,height=6,font="verdana 15 bold")
        h.pack(side=RIGHT)

nameCity=Label(frame, text="Enter the City Name",font=("Comic Sans MS", 30 ,"bold"),bg="white")
nameCity.pack()
c=StringVar
entName=Entry(frame,textvar=c,width=23,bg="palegreen",fg="black",font=("Cosmic Sans MS",18,'bold'))
entName.pack(side=LEFT)
cCity=Button(frame,text="Check",bg="palegreen",fg='black',font=("Cosmic Sans MS",15,'bold'),command=Calculate)
cCity.pack(side=RIGHT)

root.mainloop()