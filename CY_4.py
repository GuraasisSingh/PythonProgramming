'''
#Operators
a=10
b=4332
sum=a+b
print(sum)
subtract=a-b
print(subtract)
multi=a*b
print(multi)
div=a/b
print(div)
floorDiv=a//b
print(floorDiv)
expo=a**b
print(expo)
rem=a%b
print(rem)

greater=a>b
print(greater)
less=a<b
print(less)
greaterThan=a>=b
lessThan=a<=b
equal=a==b
notEqual=a!=b
print(greaterThan)
print(lessThan)
print(equal)
print(notEqual)

a=1000
print(a)
a+=1000
print(a)
a-=1000
print(a)
a*=10
print(a)
a/=3
print(a)
a//=3
print(a)
b//=21
print(b)

c=100
d=120
print(c>98 and c<130)
print(d%2==0 or d%3==0)
print(not(c>100 or c<500))
#area of right angledtriangle
h=int(input("Enter the height of the triangle"))
b=int(input("Enter the base of the triangle"))
area=0.5*h*b
print("The area of the triangle is ",area)

#Pythagoras theorem
B=int(input("Enter the Base"))
P=int(input("Enter the Perpendicular"))
H=(B*B) + (P*P)
H**=0.5
print("The Hypotenuense is ",H)

#Area of Trapezium
#1/2 * (Sum of parallel sides)*h
a=int(input("Enter the first parallel side"))
b=int(input("Enter the second parallel side"))
ht=int(input("Enter the height"))
areaTrap=0.5*(a+b)*ht
print(areaTrap)


#Celcius to Fahrenheit
#C/5=(f-32)/9
#F=((9*C)/5)+32
C=float(input("Enter the Celcius"))
F=((C*9)/5)+32
print("Fahrenheit =",F)

#Km/hr -> m/s
speedKm = float(input("Enter the speed"))
speedMs=(speedKm*5)/18
print("Speed in m/s is",speedMs)
'''
#Quadratic Equation
#ax*2+bx+c=0
#Shreedharacharya rule: x=(b+-(b*b - 4*a*c))/2a
a=float(input("Enter the value of a"))
b=float(input("Enter the value of b"))
c=float(input("Enter the value of c"))
d=4*a*c
x1= b+(((b*b) -(4*a*c)))/(2*a)
x2= b-(((b*b) -(4*a*c)))/(2*a)
print("The value of x =", x1 ,"or",x2)





























