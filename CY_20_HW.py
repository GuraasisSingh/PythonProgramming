#Session 20 HW
'''
#1.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
def subtract(a,b):
    sub=a-b
    return sub
print(subtract(a,b))
#2.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
def product(a,b):
    p=a*b
    return p
print(product(a,b))
#3.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
def modulus(a,b):
    mod=a%b
    return mod
print(modulus(a,b))
#4.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
def division(a,b):
    d=a/b
    return d
print(division(a,b))
#5.
ch=int(input("Enter choice: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division and 5 for remainder:\n"))
a=int(input("Enter first number"))
b=int(input("Enter second number"))
def addition(a,b):
    add=a+b
    return add
    
def subtract(a,b):
    sub=a-b
    return sub
    
def product(a,b):
    p=a*b
    return p
    
def division(a,b):
    d=a/b
    return d
  
def modulus(a,b):
    mod=a%b
    return mod
    
if ch==1:
    print(addition(a,b))
elif ch==2:
    print(subtract(a,b))
elif ch==3:
    print(product(a,b))
elif ch==4:
    print(division(a,b))
elif ch==5:
    print(modulus(a,b))
else:
    print("Invalid Input")
#6.
h=float(input("Enter the height of the triangle"))
b=float(input("Enter the base of the triangle"))
def areaTriangle(h,b):
    area=0.5*h*b
    return area
print(areaTriangle(h,b))

#7.
num=int(input("Enter number to be checked:\n"))
def chkPosOrNeg(n):
    if n>0:
        print("Positive")
    elif n<0:
        print("Negative")
    else:
        print("Zero")
chkPosOrNeg(num)

#8.
year=int(input("Enter the year to be checked:\n"))
def chkYear(y):
    if y%4==0 and y%100!=0:
        print("Leap Year")
    elif y%100==0:
        print("Not a Leap Year")
    elif y%400==0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
chkYear(year)

#9.
a=int(input("Enter first number:\n"))
b=int(input("Enter second number:\n"))
c=int(input("Enter third number:\n"))
def chkLargest(a,b,c):
    if a>b and a>c:
        print(a,"is greatest")
    elif b>a and b>c:
        print(b,"is greatest")           
    else:
         print(c,"is greatest")
chkLargest(a,b,c)

#10.
a=int(input("Enter first number:\n"))
b=int(input("Enter second number:\n"))
c=int(input("Enter third number:\n"))
def chkSmallest(a,b,c):
    if a<b and a<c:
        print(a,"is smallest")
    elif b<a and b<c:
        print(b,"is smallest")           
    else:
         print(c,"is smallest")
chkSmallest(a,b,c)
'''


