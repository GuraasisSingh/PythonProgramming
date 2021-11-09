'''a=['apple','mango','orange']
a[1]="kiwi"
print(a)
a[1:2]=["blueberry", "watermelon"]
print(a)

a=['apple','mango','orange','guava']
a.insert(2,"watermelon")
print(a)
a.append("kiwi")
print(a)'''

a=['apple','mango','orange','guava']
'''
b=["kiwi"]
a.extend(b)
print(a)
a.remove('apple')
print(a)
a.pop(1)
print(a)
a.pop()
print(a)
del a[0]
print(a)
#del a
#print(a)
a.clear()
print(a)

for i in a:
    print(i)
for i in range(len(a)):
    print (a[i])

i =0
while (i<len(a)):
    print(a[i])
    i+=1

[print(i) for i in a]
n=[]
for i in a :
    if  "a" in i :
        n.append(i)
print(n)


a=["apple","mango","orange","guava"]
n=[i for i in a if "gua" in i]
print(n)
h=[i for i in range(10)]
print(h)

a=["apple","mango","orange","guava"]
a.sort()
print(a)
a=[1,26,0,100,535]
a.sort(reverse=True)
print(a)'''
a=["apple","mango","orange","guava"]
b=a.copy()
print(b)
d= a
print(d)
f=list(a)
print(a)

b=[1,23,5]
c=a+b
print(c)
for i in b:
    a.append(i)
print(a)
d=a.count("apple")
print(d)
f=a.index("apple")
print(f)



