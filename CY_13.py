'''#Session 13
#1.
a=int(input("enter first number\n"))
b=int(input("enter second number\n"))
n=input("Enter your choice + to add, - to subtract * to multiply / to divide // to float divide % to remainder ** to exponent \n ")
if n=="+":
    ans=a+b
elif n=="-":
    ans=a-b
elif n=="*":
    ans=a*b
elif n=="/":
    ans=a/b
elif n=="//":
    ans=a//b
elif n=="%":
    ans=a%b
elif n=="**":
    ans=a**b
else:
    ans="invalid input"
print(ans)
'''
'''#List []
ordered
changeable/mutable

Accessing elements in a list
L to R -> 0 to +ive infinite
R to L -> -1 to -ive infinite
allow duplicate
[start : stop :step]
'''
a=[1,3.5,True,"Guraasis",'1']
print(a)
print(len(a))
print(type(a))
print(a[0])
print(a[4])
print(a[-3])
print(a[0:3])
print(a[4:0:-1])
print(a[-4:-1])
print(a[-3:])
print(a[:4])
print(a[:5])
print(a[:-1])
print(a[0::2])
print(a[:-1:3])

if '1' in a:
    print('Yes')
else:
    print('No')







    



