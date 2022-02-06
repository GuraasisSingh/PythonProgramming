#Threading:
from tkinter import *
from threading import *#emphasizing on getting values
import time

root=Tk()
root.geometry('500x300')

def threading():
    t1=Thread(target=work)
    t1.start()
def work():
    print("Sleep time starts")
    for i in range(10):
        print(i)
        time.sleep(1)
    print("Sleep time stop")
    
Button(root,text="Click Me",command=work).pack()

root.mainloop()
