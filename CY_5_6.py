#Session 5 and 6
# Jul 4, 2021
'''
#String Manipulation:
1)Creation
2)Accessing - []
3)Length
4)Count
5)Slicing [:]

s="Code Young"
print(s)
print(s[0])
print(s[-3])
print(len(s))
print(s.count('o'))
print(s[0:4])
print(s[0:11:2])
print(s[3:])
print(s[2:])
print(s[-4:-1])
print(s[:9])
print(s[:14])


#add strings
a="Guraasis"
b="Singh"
print(a+" "+b)
#reverse
a="Guraasis"
print(a[::-1])

'''
'''Conditionals :
1) if
Syntax:
if(condition):
  statement
2) if-else
if(condition):
   statement1
else:
   statement2
3) if-elif-else
if(condition):
   statement1
elif(condition2:
   statement2
else:
   statement3


num=int(input("Enter the number: "))
if(num%2==0):
    print("Even")
else:
    print("Odd")

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
ch=int(input("Enter the choice, 1 to add, 2 to subtract, 3 to multiply, 4 to divide, 5 to float divide, 6 for modulus, 7 for exponent"))
if(ch==1):
    ans=a+b
elif(ch==2):
    ans=a-b
elif(ch==3):
    ans=a*b
elif(ch==4):
    ans=a/b
elif(ch==5):
    ans=a//b
elif(ch==6):
    ans=a%b
elif(ch==7):
    ans=a**b

print(ans)
'''
#80-1000 ->Grade A
#60-80 -> Grade B
#40-60 ->Grade C
#0-40 ->Fail
# else invalid grade

grade=input("Enter the Grade:80-1000 ->Grade A, 60-80 -> Grade B,40-60 ->Grade C,0-40 ->Fail")
if(grade=='A'):
    ans="80-100"
elif(grade=='B'):
    ans="60-80"
elif(grade=='C'):
    ans="40-60"
elif(grade=='Fail'):
    ans="0-40"
else:
    ans="Invalid Grade"

print(ans)
#electricity bill
#1-100 unit -> 1.5 per unit
#101-200 units - 2.5 per unit
#201 -300 -> 4 per unit
#300-350  -> 5 per unit
#above  350, the charge is 1500
u = int(input("Enter the number of units "))
if u<=100:
    bill=u*1.5
elif u<=200:
    bill=(100*1.5) + ((u-100)*2.5)
elif u<=300:
    bill = (100*1.5)+(100*2.5)+((u-200)*4)
elif u<=350:
    bill= (100*1.5)+(100*2.5)+(100*4)+((u-300)*5)
else:
    bill = 1500

print(bill)











    
