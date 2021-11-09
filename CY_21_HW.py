'''
#Session 21 Homework
#1.
p=float(input("Enter the principle:\n"))
t=int(input("Enter the no of years:\n"))
r=float(input("Enter the rate of interest:\n"))
def simpleInterest(p,t,r):
    si=(p*t*r)/100
    return si
print("The Simple Interest is:\n",simpleInterest(p,t,r))
#2.
p=float(input("Enter the principle:\n"))
t=int(input("Enter the no of years:\n"))
r=float(input("Enter the rate of interest:\n"))
def compoundInterest(p,t,r):
    ci=(p*((1+r/100)**t))-p
    return ci
print("The Compound Interest is:\n",compoundInterest(p,t,r))

#3.
print("Square")
s=float(input("Enter the side of square:\n"))
print("Rectangle")
l=float(input("Enter the length of rectangle:\n"))
b=float(input("Enter the breadth of rectangle:\n"))
print("Triangle")
h=float(input("Enter the height of triangle:\n"))
ba=float(input("Enter the base of triangle:\n"))
def area2D(s,l,b,h,ba):
    sq=s*s
    print("Area of square is",sq)
    rec=l*b
    print("Area of rectangle is",rec)
    tri=0.5*ba*h
    print("Area of Triangle is",tri)
area2D(s,l,b,h,ba)
'''
#4.
e=float(input("Enter the edge of a Cube:\n"))
l=float(input("Enter the length of a Cuboid:\n"))
b=float(input("Enter the breadth of a Cuboid:\n"))
h=float(input("Enter the height of a Cuboid:\n"))
ht=float(input("Enter the height of a Cylinder:\n"))
r=float(input("Enter the radius of a Cylinder:\n"))
def area3D(e,l,b,h,ht,r):
    cube=e**3
    print("Volume of cube =",cube)
    cuboid=l*b*h
    print("Voulume of cuboid =",cuboid)
    cylin=(22/7)*r*ht
    print("Voulume of cylinder =",cylin)
area3D(e,l,b,h,ht,r)



    







