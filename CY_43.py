"Messenge Box"
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("300x250")

'''
w=Label(root,text="Welcome",font="30")
w.pack()

messagebox.showinfo("showinfo","Content")
messagebox.showwarning("showinfo","Warning")
messagebox.showerror("showinfo","Error")
messagebox.askquestion("showinfo","How are you? Are you doing well")
messagebox.askokcancel("showinfo","Calculate the output?")
messagebox.askyesno("showinfo","Would you like to have the coffee?")
messagebox.askretrycancel("showinfo","Try again?")
#c=messagebox.askretrycancel("showinfo","Try again?")->putting in a variable
root.mainloop()
'''
'''#configuring according to butt
def b1():
    messagebox.askretrycancel("showinfo","Try again?")
    
b=Button(root,text="Button-1",command=b1)
b.pack()
'''
s=StringVar()
s.set("HII")
m=Message(root,textvariable=s,relief=RAISED)
m.pack()
root.mainloop()
