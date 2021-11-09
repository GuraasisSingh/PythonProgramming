#session 5 and 6 hw
#1.
a="Guraasis"
b="Singh"
print((a[::-1])+(b[::-1]))
#2.
#80-1000 ->Grade A
#60-80 -> Grade B
#40-60 ->Grade C
#0-40 ->Fail
# else invalid grade
m=int(input("Enter the marks:80-100 ->Grade A, 60-80 -> Grade B,40-60 ->Grade C,0-40 ->Fail"))
if(m>=80 and m<=100):
    grade='A'
elif(m>=60 and m<80):
    grade='B'
elif(m>=40 and m<60):
    grade='C'
elif(m>=0 and m<40):
    grade='Fail'
else:
    grade="Invalid Marks"

print(grade)

#3.
q=int(input("Enter the quantity in KG"))
price=1000
if(q>500):
      d=100
elif(q==500):
    d=75
elif(q<500):
    d=50
price-=d
print(price)
