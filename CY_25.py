'''
#Session 25
#os module deals with current working directory
import os
#f=open("E:\GURAASIS\Python Codeyoung/abc.txt","x")# to be executed once only
#f=open("E:\GURAASIS\Python Codeyoung/abc.txt","w")error
f=open("E:\GURAASIS\Python Codeyoung/bg.txt","w")
cwd=os.getcwd()
print(cwd)
def c_p():
    print("Before")
    print(os.getcwd())
    print()
c_p()
os.chdir("../")
print("After")
c_p()

import os
os.remove("E:\GURAASIS\Python Codeyoung/abc.txt")

import os
if os.path.exists("bgg.txt"):
    os.remove("bgg.txt")
else:
    print("The file does not exist")
'''
#import os
#os.rmdir("E:\GURAASIS\Python Codeyoung/CY")use only once to avoid any error
#............................................................

#String functions
a="Guraasis@is@a@great@person"#returns in a list
g=a.split("@")
print(g)
a="Guraasis is a great person"#returns in a list
g=a.split()
print(g)

a="For only {price:2f} dollars"#used curly brackets
print(a.format(price=50))
a="For only {price:.2f} dollars"#used curly brackets
print(a.format(price=49))
a="For only {price:.4f} dollars"#used curly brackets
print(a.format(price=49))
a="For only {price} dollars"#used curly brackets
print(a.format(price=49))


a="My name is {fname}, I am {age}".format(fname="Sakshi",age=22)
b="My name is {0},I am {1}".format("John",50)
c="My name is {}, I am {}".format("Sarah",25)
print(a)
print(b)
print(c)

