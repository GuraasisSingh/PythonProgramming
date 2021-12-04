#Session 40
"""
#ComboBox
import tkinter as tk
from tkinter import ttk#used for combo box
window=tk.Tk()
window.title("COMBO BOX")
window.geometry("300x200")

ttk.Label(window,text="This is Combo Box",background="gold",foreground="red",font=("Times New Roman",10)).grid(row=0,column=1)
ttk.Label(window,text="Select a month: ",background="gold",foreground="red",font=("Times New Roman",10)).grid(row=5,column=0,padx=10,pady=25)

n=tk.StringVar()
monthchoosen=ttk.Combobox(window,width=27,textvariable=n)
monthchoosen["values"]=("JAN",
                        "FEB",
                        "MARCH",
                        "APRIL",
                        "MAY",
                        "JUNE",
                        "JULY",
                        "AUG",
                        "SEPT",
                        "OCT",
                        "NOV",
                        "DEC")

monthchoosen.grid(column=1,row=5)
monthchoosen.current()
window.mainloop()
"""
'''
#ScrollText
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
window=tk.Tk()
window.title("SCROLLED TEXT")
window.geometry("300x200")

ttk.Label(window,text="SCROLLED TEXT",background="gold",foreground="red",font=("Times New Roman",10)).grid(row=0,column=1)

text_area=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=10,height=5,font=("Times New Roman",15))
text_area.grid(column=0,pady=10,padx=10)
text_area.insert(tk.INSERT,"""\Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!""")

text_area.focus()
text_area.configure(state="disabled")#not be able to write 
window.mainloop()
'''
'''
#Notebook
from tkinter import *
from tkinter import ttk
window=Tk()
window.title("NOTEBOOK!!!")
window.geometry("300x200")

n=ttk.Notebook(window)
n.pack(expand=1,fill=BOTH)

t1=ttk.Frame(n)
n.add(t1,text="TAB 1")
t2=ttk.Frame(n)
n.add(t2,text="TAB 2")

Label(t1,text="hello",font=("Times New Roman",15)).pack()
Label(t2,text="bye",font=("Times New Roman",15)).pack()

window.mainloop()
'''
