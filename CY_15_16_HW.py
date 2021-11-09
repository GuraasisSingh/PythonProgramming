'''
#Homework Session 15 and 16
#1) Write a program to take sample credit card numbers as input and validate it with existing tuple of credit card numbers
card=(123456789087,567890437896)
a=int(input("Enter 1st credit card number"))
b=int(input("Enter 2nd credit card number"))
c=(a,b)
if (c==card):
    print("Correct credit card numbers")
else:
    print("Incorrect Credit card numbers")
#2) Write a program to insert only positive numbers to a list
a=[]
num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
b=[num1,num2]
for i in b:
    if i > 0:
        a.append(i)
print(a)

#3) Write a program to edit tuples 
#Hint: Convert a tuple to a list, edit and then convert back to a tuple
a=("apple","mango","banana","papaya")
b=list(a)
b[1]="kiwi"
b.append("orange")
b.remove("apple")
a=tuple(b)
print(a)

#4) Write a program to change all even numbers to odd and odd numbers to even in a list
numlist=[1,23,43,16,17,18]
nlist=[]
for i in numlist:
    i+=1
    nlist.append(i)
print(nlist)

#5) Write a program to take all prime numbers from a list and add to a new list
#Hint: From a list of natural numbers, check which numbers are prime and add to a new list
natural=[1,2,3,4,5,6,7,8,9,10]
prime=[]
for i in natural:
    t=0
    for j in range(1,i+1):
        if i%j==0:
            t+=1
    if t==2:
        prime.append(i)
print(prime)

#6) Write a program to perform intersection and complement operation on a set without using inbuilt
a={1,2,3}
b={3,4,5}
c=set()
for i in a:
    if {i}.issubset(b):
        c.add(i)
print(c)

#7) Implement all the Tuple operations
a=(1,True,3.5,'apple',1)
print(a)
print(len(a))
print(type(a))
b=(a,8.9)
print(b)
print(a[3])
print(a[-3])
if "apple" in a:
    print("yes!")
a=("apple","mango")
b=list(a)
b[1]="kiwi"
b.append("orange")
b.remove("apple")
a=tuple(b)
print(a)
f=("grapes",)#single element with a comma 
a+=f
print(a)
#del a 
print(a)
#8) Implement all the Dictionary operations
a={
    1:'a',
    2:'b',
    3:'c',
    "apple":4
}
print(a)
print(len(a))
print(type(a))
print(a.keys())
print(a.values())
print(a.items())
print(a[1])
print(a.get("apple"))
a['apple']='white'
a['apple']='white'
print(a)
if "apple" in a:
    print("Yayy!!")
a.update({"green":2021})
print(a)
a.pop("apple")
print(a)
a.popitem()
print(a)
del a[1]
print(a)
#del a
#a.clear()
print(a)
#9) Implement all the Set operations
a={"apple","mango","grapes"}
a.add("kiwi")
print(a)
b={"blueberry"}
a.update(b)
print(a)
a.remove("apple")#error if "" not present
print(a)
a.discard("mango")#no error whether present or not
a.pop()#removes last element but we cannot exactly specify
print(a)
a.clear()
print(a)
# del a
'''
