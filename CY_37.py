#Session 37
'''
from tkinter import *
root=Tk()
v=IntVar()
Radiobutton(root,text="HELLO",variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="BYE",variable=v,value=2).pack(anchor=W)
#Radiobutton(root,text="BYE",variable=v,value=2).pack(anchor=E)
#Radiobutton(root,text="BYE",variable=v,value=2).pack(anchor=N)
#Radiobutton(root,text="BYE",variable=v,value=2).pack(anchor=S)
Radiobutton(root,text="HI",variable=v,value=2).pack(anchor=NE)
root.mainloop()
'''
'''
#Canvas:
from tkinter import *
root=Tk()
root.geometry("350x250")
root.config(bg="gold")
w=Canvas(root,width=40,height=60,bg="red")
w.pack()
ch=20
cw=200
y=int(ch/2)
w.create_line(0,y,cw,y)
root.mainloop()
'''
'''
from tkinter import *
root=Tk()
root.title("CREATE LINES!")
root.geometry("450x350")
root.config(bg="gold")
w=Canvas(root,width=300,height=200,bg="red")
w.pack()
w.create_rectangle(50,150,200,50,fill="blue")
#w.create_oval(50,150,200,50,fill="blue")
root.mainloop()
'''
'''
from tkinter import *
root=Tk()
root.geometry("550x550")
root.config(bg="gold")
w=Canvas(root,width=300,height=200,bg="red")
w.pack()
w.create_polygon(50,150,200,50,45,78,43,77,fill="blue")
root.mainloop()
#eleven sided polygon-hendecagon
#twelve sided polygon-dodecagon
#thirteen sided polygon-tridecagon
#twenty sided polygon-icosagen
#thirty sided polygon-tricontagon
#forty sided polygon-tetracontagon
#fifty sided polygon-pentacontagon
'''
'''
#Frame:
from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()
root.title("Frames!")
root.geometry("350x250")
root.config(bg="gold")
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
g=Button(frame,text="RED",fg="WHITE",bg="red")
g.pack(side=LEFT)
r=Button(frame,text="GREEN",fg="WHITE",bg="GREEN")
r.pack(side=BOTTOM)
root.mainloop()
'''
#make three buttons in top frame(yellow,red,blue) and 1 green in bottom
#implement all we have learnt
