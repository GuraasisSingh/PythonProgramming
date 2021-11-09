#Session 24 HW
'''
#1.
f=open("E:\GURAASIS\Python Codeyoung/abc.txt","w")
f.write("hi\nhow aren you\nwhat are you doing\nare you fine\nDo you like programming")
f.close()
f=open("E:\GURAASIS\Python Codeyoung/q1.txt","r")
print(f.read())

#2.
f=open("E:\GURAASIS\Python Codeyoung/para.txt","r")
for x in f:
    print(f.readline())
f.close()

#3.
f=open("E:\GURAASIS\Python Codeyoung/infobasic.txt","r")
for x in f:
    print(f.readline())
    if x==15:
        break
f.close()

#4.
f=open("E:\GURAASIS\Python Codeyoung/parapoem.txt","r")
for x in f:
    print(x)
f.close()

#5.
f=open("E:\GURAASIS\Python Codeyoung/hello.txt","w")
f.write("Hey, now i can write file in python!!")
f.close()
f=open("E:\GURAASIS\Python Codeyoung/hello.txt","r")
print(f.read())
f.close()

#6.
f=open("E:\GURAASIS\Python Codeyoung/hello.txt","a")
f.write("Hey, now i can add something to this file in python!!")
f.close()
f=open("E:\GURAASIS\Python Codeyoung/hello.txt","r")
print(f.read())
f.close()
'''
