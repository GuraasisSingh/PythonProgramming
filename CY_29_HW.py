import random
#Session 29 HW
#1.
'''
n=int(input("Enter a number:\n"))
largest=0
m=n
while m>0:
    c=m%10
    if c>largest:
        largest = c
    m//=10
print("The largest value in",n,"is",largest)
'''
'''
#2.
n=int(input("Enter a number:\n"))
smallest=9
m=n
while m>0:
    c=m%10
    if c<smallest:
        smallest = c
    m//=10
print("The smallest value in",n,"is",smallest)
'''
'''
#3.
n=int(input("Enter a number:\n"))
def strongNum(n):
   s=0
   m=n
   while n>0:
       r=n%10
       f=1
       for i in range(1,r+1):
           f=f*i
       s+=f
       n=n//10
        
   if s==m:
       print(m,"is a strong number")
   else:
       print(m,"is not a strong number")
        
strongNum(n)
'''
'''
#4.
def strongNum(n):
   s=0
   m=n
   while n>0:
       r=n%10
       f=1
       for i in range(1,r+1):
           f=f*i
       s+=f
       n=n//10
        
   if s==m:
       print(m,"is a strong number")
   else:
       print(m,"is not a strong number")

List=[1,145,234,2,40585,6]        
for i in List:
    strongNum(i)        
'''
'''
#5.
def otpGenerator():
    otp=""
    for i in range(1,7):
        otp+=str(random.randint(1,9))
    print("Your six digit OTP is :",otp)
otpGenerator()
'''




