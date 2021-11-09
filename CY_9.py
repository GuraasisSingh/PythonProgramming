'''session control:
loops:
Nested loops:
Loop inside a loop
1)for inside for
Syntax :
for iterating_sequence in sequence:
    for iterating_sequence in sequence:
        statement
    statement
2)while inside while

'''
'''color=['red','green','yellow']
fruits=['apple','grapes','mango']
for i in color:#outer
    for j in fruits:#inner
        print(i,j)

i=1#            initialization
while(i<=3):#   condition
    print(i,"Outer loop is executed only once")
    j=1
    while(j<=3):
        print(j,"Inner loop is executed until completion!")
        j+=1
    i+=1#       update statements
'''
'''n=0
for i in range(1,11):
   if(n==0):
       print("Not valid")
    elif(n<0):
        print("Invalid Input")
    else:
        print(n*i)
'''
n=int(input("Enter the number :"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=(rev*10)+dig
    n//=10

if(rev==temp):
    print("Palindrome")
else:
    print("Not palindrome")



