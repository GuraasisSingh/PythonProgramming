#Session 11 and 12 HW
#1.
for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print(i,end=" ")
        else:
            print(" ", end=" ")
    print()
#2.
for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print(j  ,end=" ")
        else:
            print(" ", end=" ")
    print()
#3.
for i in range(1,6):
    for j in range(1,6):
        if(i<=6-j):
            print(i,end=" ")
        else:
            print(" ", end=" ")
    print()
#4.
for i in range(1,6):
    for j in range(1,6):
        if(i<=6-j):
            print('5',end=" ")
        else:
            print(" ", end=" ")
    print()
#5.
for i in range(0,6):
    for j in range(0,6):
        if(i<=5-j):
            print(j,end=" ")
        else:
            print(" ", end=" ")
    print()
#6.
k=1
for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print(k,end=" ")
        else:
            print(" ", end=" ")
    print()
    k+=2
i=1
while i<=5:
    j=1
    while(j<=i):
        print((i*2 - 1), end=" ")
        j+=1
    i+=1
    print()
#7.
for i in range(1,6):
    for j in range(1,6):
        if(i<=6-j):
            print(6-i,end=" ")
        else:
            print(" ", end=" ")
    print()
#8.
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print(" ")
#9.
for i in range(5,0,-1):
    for j in range(i,0,-1):               
        print(j, end=" ")
    print()
#10.
for i in range(1,5):
    for j in range(1,8):
        if(j>=5-i and j<=3+i):
            print('*',end=" ")
        else:
            print(" ", end=" ")        
    print()











    
