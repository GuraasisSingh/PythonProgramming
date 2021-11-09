#Session 24
#FILE HANDLING
"""
open(filename,mode)
1)Open a file
2)Read/Write
3)Close the file

Modes:
r read
w write
a append
r+ reading nd writing
x create

f=open("E:\GURAASIS\Python Codeyoung/hello.txt","r")
print(f.read())

f=open("E:\GURAASIS\Python Codeyoung/hello.txt","r")
print(f.read(5))
print(f.readline())
print(f.readline())

f=open("E:\GURAASIS\Python Codeyoung/hello.txt","r")
for x in f:
    print(x)
f.close()

f=open("E:\GURAASIS\Python Codeyoung/hello.txt","a")
f.write("Now the file is overwritten!")
f.close()
f=open("E:\GURAASIS\Python Codeyoung/hello.txt","r")
print(f.read())
"""
f=open("E:\GURAASIS\Python Codeyoung/hello.txt","w")
f.write("Now the file content is deleted!")
f.close()
f=open("E:\GURAASIS\Python Codeyoung/hello.txt","r")
print(f.read())
