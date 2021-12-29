#Session 36 HW

#A Design like Notepad Menu
from tkinter import *
root=Tk()
root.title("Untitled - Notepad")
root.geometry("500x500")
root.config(bg="white")
menu=Menu(root)
item1=Menu(menu)
item2=Menu(menu)
item3=Menu(menu)
item4=Menu(menu)
item5=Menu(menu)

menu.add_cascade(label="File",menu=item1)
item1.add_command(label="New                                   Ctrl+N")
item1.add_command(label="New Window         Ctrl+Shift+N")
item1.add_command(label="Open...                               Ctrl+O")
item1.add_command(label="Save                                    Ctrl+S")
item1.add_command(label="Save As...                 Ctrl+Shift+S")
item1.add_separator()
item1.add_command(label="Page Setup...")
item1.add_command(label="Print...                                Ctrl+P")
item1.add_separator()
item1.add_command(label="Exit")

menu.add_cascade(label="Edit",menu=item2)
item2.add_command(label="Undo                                               Ctrl+Z")
item2.add_separator()
item2.add_command(label="Cut                                                  Ctrl+X")
item2.add_command(label="Copy                                               Ctrl+C")
item2.add_command(label="Paste                                               Ctrl+V")
item2.add_command(label="Delete                                                  Del")
item2.add_separator()
item2.add_command(label="Search with Bing                           Ctrl+E")
item2.add_command(label="Find...                                              Ctrl+F")
item2.add_command(label="Find Next                                              F3")
item2.add_command(label="Find Previous                             Shift+F3")
item2.add_command(label="Replace...                                       Ctrl+H")
item2.add_command(label="Go To...                                          Ctrl+G")
item2.add_separator()
item2.add_command(label="Select All                                       Ctrl+A")
item2.add_command(label="Time/Date                                            F5")

menu.add_cascade(label="Format",menu=item3)
item3.add_command(label="Word Wrap")
item3.add_command(label="Font...")

menu.add_cascade(label="View",menu=item4)
item4.add_command(label="Zoom")
item4.add_command(label="Status Bar")

menu.add_cascade(label="Help",menu=item5)
item5.add_command(label="View Help")
item5.add_command(label="Send Feedback")
item5.add_separator()
item5.add_command(label="About Notepad")

root.config(menu=menu)
root.mainloop()


