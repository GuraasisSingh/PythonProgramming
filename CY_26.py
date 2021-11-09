'''
#Session 26
s=input("Enter a number:\n")
fs=int(s[0])
ls=int(s[-1])
a=fs+ls
print(a)

n=int(input("Enter the number:\n"))
rem=n%10
while(n>9):
    n//=10
rem+=n
print(rem)

import calendar
yy=2021
mm=11
print(calendar.month(yy,mm))
#print(calendar.calendar(2018))
print(calendar.calendar(2018,2,1,6))
d=calendar.Calendar(firstweekday=0)
for day in d.iterweekdays():
    print(day)
h=calendar.Calendar()
for l in h.itermonthdates(2012,9):
    print(l)
'''
a=12
b=23
c=56
print(min(a,b,c))
print(max(a,b,c))
import math
print(math.ceil(2.0))
print(math.floor(1.4))
print(math.pow(2,4))
p=math.pi
r=10
print(p*r*r)
print(abs(-3))
print(math.isqrt(7))#nearest root value in integer
print(math.sqrt(49))
s=(1,4,6)
print(math.prod(s))
print(math.radians(180))
print(math.remainder(9,2))
print(math.trunc(2.77))#removes the decimals
a=7
b=2
print(math.perm(a,b))



