for i in range(1,5):#outer loop-how many times-row
    for j in range(1,5):
        print("*", end=" ")
    print()
for i in range(1,5):#outer loop-how many times
    for j in range(1,5):#column - what to 
        print("*", end =' ')
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print('*', end=' ')
    print()
for i in range(1,5):
    for j in range(1,5):
        if(j<=i):
            print('*',end=" ")
        else:
            print("#", end=" ")
    print()
for i in range(1,5):
    for j in range(1,5):
        if(j>=5-i):
            print('*',end=" ")
        else:
            print(" ", end=" ")
    print()
'''
   *
  ***
 *****
*******
'''
for i in range(1,5):
    for j in range(1,8):
        if(j>=5-i and j<=3+i):
            print('*',end=" ")
        else:
            print(" ", end=" ")
        
    print()
for i in range(1,5):
    for j in range(1,5):
        if(j>=5-i):
            print('*',end=" ")
        else:
            print(" ", end=" ")
        
    print()


for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print(" ")

