#Session 42
'''
#Date and time module
from datetime import date
from datetime import datetime
d=date(1999,6,16)
print("Date passed as argumnent is ",d)
t=date.today()
print("Today's date: ",t)
print("Current year",t.year)
print("Current month",t.month)
print("Current day",t.day)
dt=datetime.fromtimestamp(1886473552)
print("Datetime of the timestamp",dt)
s=date.isoformat(t)
print("String representation",s)
print(type(s))
'''
'''
from datetime import time
t=time(13,24,56)
print("Entered time:",t)
to = time(minute=12)
print(to)
g=time()
print("time without argument",g)
print("minute :",t.minute)
print("Hour :",t.hour)
print("Second :",t.second)
h=time(12,34,55,1223)
s=h.isoformat()
print("String representation",s)
print(type(s))
'''
import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
d=datetime.datetime(2021,4,30)
print(d)
print(x.strftime("%A"))#->name of the day eg-Sunday
print(x.strftime("%a"))#->name of the day in short form eg-Sun
print(x.strftime("%w"))#weekday as a number 0-6
print(x.strftime("%d"))#day, 1-31
print(x.strftime("%b"))#month name short version
print(x.strftime("%B"))#month name full version
print(x.strftime("%m"))#month as a number
print(x.strftime("%y"))#year short version
print(x.strftime("%Y"))#year full version
#H, I ,p, M ,S, f ,z ,j ,U , W , c ,x ,X,G,u ,V -> try these
#tkinter program, take wt in kg, convert to grams


