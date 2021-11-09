'''
Control Flow: Loop Control-
#session 10
1)break statement
FOR----
for var in sequence:
    if condition:
        break
WHILE----
while(test expression):
    if(condition):
    break
n=5
while (n>0):
    n-=1
    if(n==2):
        print("Loop terminated")
        break
    print(n)
2)continue statement
s="Hi,Welcome to Codeyoung"
for i in s:
    if(i=='C'):
        print("Skipping")
        continue
    print(i)
n=5
while (n>0):
    n-=2
    if(n==1):
        print("Skipped")
        continue
    print(n)
3)pass statement-null operation
Used - writing empty loop
s="Codeyoung"
for i in  s:
    if(i=="y"):
        print ("Pass is executed")
        pass
    print(i)
for i in range(0,11):
    pass
'''
'''s="CodeYoung"
for i in s:
    if(i=='Y'):
        print("Terminating the loop!")
        break
    print(i)
'''

    










    
