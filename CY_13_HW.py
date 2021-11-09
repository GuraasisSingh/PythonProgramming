#Session 13 HW
#1.
'''
a=[1,3.5,True,"Guraasis",'1']
print(a)
print(len(a))
print(type(a))
print(a[4:0:-1])
if '1' in a:
    print('Yes')
else:
    print('No')'''
#2.
'''
parallelogram
num=int(input("Enter the number"))
for i in range(num,0,-1):
    for j in range(1,i):
        print(' ',end="")
    for k in range(0,num):
        print('*',end="")
    print()
'''
#3.
sq=1
for i in range(1,7):
        print(sq)
        sq*=11
#4.
n = int(input("Enter the number "))

for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(1, 2*i):
        print("*", end="")
    print()
for i in range(2, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(1, 2*i):
        print("*", end="")
    print()
