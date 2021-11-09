#Session 26 HW
import math
#1.
'''
s=input("Enter the String:\n")
print(s.title())
'''
'''
#join()-concatenates
s=input("Enter the String:\n")
print("Original string",s)
r=' '.join(e.capitalize() for e in s.split())
print(r)
'''
'''
import string
s=input("Enter any String:\n")
print("Original String",s)
r=string.capwords(s)
print(r)
'''
#2.
'''
s1=input("Enter the String:\n")
first=s1[0]
last=s1[-1]
swap=last +(s1[1:-1]) + first
print(swap)
'''
#3.
'''
myList=[1,2,34,5,6]
List=myList[0],myList[-1]
print(List)
'''
#4.
'''
num=int(input("Enter the number to be checked:\n"))
def chkPronic(num):
    i=0
    while (i<=int(math.sqrt(num))):
        if(num ==((i*i)+(i*1))):
            return True
        i=i+1
    return False
if chkPronic(num):
    print(num,"is a pronic number")
else:
     print(num,"is not a pronic number")
'''
