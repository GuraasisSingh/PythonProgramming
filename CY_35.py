#Session 35
"""GUI(Data Abstraction)
allows to interact with user
why? use graphics and make interactive

->just moving pointer and clicking like desktop icon

Libraries:
>Kivy
>Python QT
>wxPython
>Tkinter -most commonly used

"""
"""
from tkinter import *
#* means import everything(all classes, functions and variables)
root=Tk()
root.geometry("300x100")#set the dimension of tkinter window
root.config(bg="gold")
root.title("GUI")

a=Label(root,text="Hello! World",bg="red",fg="white")
#fg- foreground colour
a.pack()# by default to top
#a.pack(side=LEFT)->packs towards left
#a.pack(side=RIGHT)->packs towards right
#a.pack(side=BOTTOM)->packs towards bottom
#a.pack(side=TOP)->packs towards top

#pack-geometry manager

root.mainloop()
#stays in loop until we close it
"""
