'''
Session 22
def sum(a,b):
    print(a+b)
sum(1,4)
#parameters are defined in the function declaration
#arguments are defined in method call
Types of Arguments:
1) Postional Argument
2) Keyword Argument

#positional
def p(f,l):#postional argumnets as when we change the position of arguments, like l,f the program changes
    print(f+" "+l)
p("Guraasis","Singh")
#Keyword
def p(l,f):
    print(f+" "+l)
p(f="Guraasis",l="Singh")

def a():
    pass

Recursion :
A defined function can call itself


def t(k):
    if k>0:
        r=k+t(k-1)
        print(r)
    else:
        r=0
    return r
print("Recursion Example Result")
t(6)
'''

def fact(n):
    if (n==1):
        return 1
    else:
        return(n*fact(n-1))

def fact(n):
    if (n==1):
        return 1
    else:
        return(n*fact(n-1))
x=fact(3)
num=3
print("The factorial of", num ,"is",fact(num))




