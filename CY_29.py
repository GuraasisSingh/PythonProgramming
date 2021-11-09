#Session 29
'''
Global and Local Variable


#Local Variable
def f():
    #local variable
    s="Coding"
    print(s)
f()
print(s)

#Global Variable
def g():
    print("Inside function: ",s)
s="I like Coding!"
g()
print("Outside the function:",s)

#Global Variable
def f():
    s="hello"
    print(s)
s="I like Coding!"
f()
print(s)

#Global Variable
def f():
    global s
    s+="hello"
    print("Inside a function",s)
s="I like Coding!"
f()
print(s)
'''
'''
a=1
def f():
    print("Inside f():",a)#1
def g():
    a=2
    print("Inside g():",a)#2
def h():
    global a
    a=3
    print("Inside h():",a)#3
print("Global: ",a)#1
f()#1
print("Global: ",a)#1
g()#2
print("Global: ",a)#1
h()#3
print("Global: ",a)#3
'''
