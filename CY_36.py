'''
from tkinter import *
root=Tk()
root.title("Welcome to Gui Tkinter")
root.geometry("290x200")
root.config(bg="gold")
menu=Menu(root)
item=Menu(menu)
menu.add_cascade(label="File",menu=item)
item.add_command(label="New")
item.add_command(label="Open")
item.add_command(label="Save")
item.add_command(label="Save as")
item.add_command(label="Close")
item.add_separator()
item.add_command(label="Exit")


root.config(menu=menu)
def click():
    l1.configure(text="The button got clicked!")
    

l1=Label(root,text="Are you a technophile?",bg="cadet blue",fg="black")
l1.grid(row=0,column=1)

l2=Entry(root,bg="red",fg="white",width=4)
l2.grid(row=3,column=3)

b1=Button(root,text="Click me!",fg="red",bg="green",command=click)
b1.grid(row=5,column=5)
root.mainloop()

#One geometry manager for entire program(pack or grid)
'''

from tkinter import *
root= Tk()
v1=IntVar()
v2=IntVar()
#Checkbutton(root,text="Hello",variable=v1).grid(row=0,column=1)
#Checkbutton(root,text="Bye",variable=v2).grid(row=0,column=2)
Radiobutton(root,text="Hello",variable=v1).grid(row=0,column=1)
Radiobutton(root,text="Bye",variable=v2).grid(row=0,column=2)
root.mainloop()




