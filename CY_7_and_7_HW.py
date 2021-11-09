'''s1=(input("Enter first string"))
s2=(input("Enter second string"))
if (len(s1))==(len(s2)):
    print("Strings are equal")
else:
    print("Strings are not equal")
'''
'''#simple interest
p=(input("Enter principle")
t=(input("Enter time")
r=(input("Enter rate")
ch=int((input("Enter choice, one for simple interest and 2 for compound interest"))
if(ch==1):
    si=(p*t*r)/100
    print(si)
#compound interesr
elif(ch==2):
    a=p*((1+(r/100))**t)
    ci=a-p
    print(ci)
else:
    print("Invalid choice")
'''
'''#>30<50
#>0<30
temp=float(input("Enter temperature"))
if(temp>=30 and temp <=60):
    print("summer")
elif(temp>=0 and temp<30):
    print("winter")
else:
    print("Invalid temperature")
'''
#hw
#1.ch=int((input("Enter choice, one for area of square, 2 for area of rectangle , 3 for isosceles,  4 equilateral, 5 for scalene ,6 for circle and 7 for semi circle "))
#2. choice finding the volumen 1-sphere 2-hemishepher 3-cone 4-cylinder
#1
ch=int(input("Enter choice, one for area of square, 2 for area of rectangle , 3 for isosceles,  4 equilateral, 5 for scalene ,6 for circle and 7 for semi circle "))
if ch==1:
    sqSide=float(input("Enter the value of side"))
    area= sqSide**2
    print(area)
elif ch==2:
    a=float(input("Enter the value of length"))
    b=float(input("Enter the value of breadth"))
    area=a*b
    print(area)
elif ch==3:
    b=float(input("Enter the value of height"))
    h=float(input("Enter the value of base"))
    area = 0.5 * h*b
    print(area)
elif ch==4:
    a=float(input("Enter the value of side "))
    area=((3**0.5)/4)*(a*a)
    print(area)
elif ch==5:
    a=float(input("Enter the value of side 1"))
    b=float(input("Enter the value of side 2"))
    c=float(input("Enter the value of side 3"))
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print(area)
elif ch==6:
    r=float(input("Enter the value of radius"))
    area=((22/7)*r*r)/2
    print(area)
elif ch==7:
    r=float(input("Enter the value of radius"))
    area=((22/7)*r*r)/2
    print(area)
else:
    print("Invalid choice")
#2
ch=int(input("Enter choice to find volume of different bodies ,1-sphere 2-hemishepher 3-cone 4-cylinder"))
if ch==1:
    r=float(input("Enter the value of radius"))
    vol=(4/3)*(22/7)*r*r*r
    print(vol)
elif ch==2:
    r=float(input("Enter the value of radius"))
    vol=(2*(22/7)*(r**3))/3
    print(vol)
elif ch==3:
    r=float(input("Enter the value of radius"))
    h=float(input("Enter the value of heigth"))
    vol=(1/3)*(22/7)*r*r*h
    print(vol)
elif ch==4:
    r=float(input("Enter the value of radius"))
    h=float(input("Enter the value of heigth"))
    vol=(22/7)*r*r*h
    print(vol)
else:
    print("Invalid Choice")
'''a=10
b=20
temp=a
a=b
b=temp
print(a,b)
a=30
b=20
a=a+b
b=a-b
a=a-b
print(a,b)
a=20
b=10
a=a*b
b=a/b
a=a/b
print(a,b)
'''






