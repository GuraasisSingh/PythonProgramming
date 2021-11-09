#Session 21
'''
num=int(input("Enter the number:\n"))
def multiplicationTable(num):
    for i in range(1,11):
        print(num,"*",i,"=",(num*i))
multiplicationTable(num)

num=int(input("Enter any number"))
def countFactors(num):
    factor=1
    count=0
    while(factor<=num):
        if(num%factor==0):
            count+=1
        factor+=1
    return count
print(countFactors(num))

num=int(input("Enter any number"))
def countFactors(num):
    factor=1
    count=0
    while(factor<=num):
        if(num%factor==0):
            count+=1
        factor+=1
    return count

num=int(input("Enter any number:\n"))
def prime(num):
    i=1
    count=0
    while(i<=num):
        if(num%i==0):
            count+=1
        i+=1
    if (count==2):
        print("Prime")
    else:
        print("Not Prime")
prime(num)

s=input("Enter the string:\n")
def lettersOfString(s):
    s=s.upper()
    letters=set()
    for i in s:
        letters.add(i)
    return letters
print(lettersOfString(s))
'''



