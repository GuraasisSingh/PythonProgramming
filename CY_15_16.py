'''
Tuple:()
ordered
immutable/ unchangable
allow duplicates

a=(1,True,3.5,'apple',1)
print(a)
print(len(a))
print(type(a))
b=(a,8.9)
print(b)
print(a[3])
print(a[-3])
if "apple" in a:
    print("yes!")
a=("apple","mango")
b=list(a)
b[1]="kiwi"
b.append("orange")
b.remove("apple")
a=tuple(b)
print(a)
g=("grapes",)#single element with a comma 
a+=g
print(a)
#del a 
print(a)

a=("apple","mango","kiwi","blueberry","watermelon")#packing a tuple
(red,yellow,*green)=a
#unpacking a tuple
print(green)
print(yellow)
print(red)
for i in a :
    print(i)
for j in range(len(a)):
    print(a[j])
i=0
while (i<len(a)):
    print(a[])
    i+=1

a=("apple","mango","kiwi","blueberry","watermelon")#packing a tuple
b=("orange",)
c=a+b
print(c)
print(b*4)
print(a.count("apple"))
print(a.index("apple"))


lists are mutable and tuple is immutable
lists  are good in performing addition subtraction, tuple for accessing element
lists get more memory , tuple less
lists have several built in methods, whereas tuple dont have many
iteration in lists is time consuming, tuple iteration is faster
unexpected errors in lists more, less errors in tuple
A list is mutable, tuple is immutable


#Set{}

unordered
immutable
duplicatesare not allowed

a={1,3.5,1,"apple"}
print(a)
print(len(a))
print(type(a))

for i in a:
    print(i)
print("apple" in a)

a={"apple","mango","grapes"}
a.add("kiwi")
print(a)
b={"blueberry"}
a.update(b)
print(a)
a.remove("apple")#error if "" not present
print(a)
a.discard("mango")#no error whether present or not
a.pop()#removes last element but we cannot exactly specify
print(a)
a.clear()
print(a)
# del a
for i in a:
    print(i)
a={"apple","mango","grapes"}
b={"kiwi","apple"}
print(a.union(b))
print(a.intersection(b))
#set.copy()
#set.difference(set)
#set.difference_update(set) #removes intersection
#set.intersection_update()  #removes item not present in both sets
#set.isdisjoint(set)
#set.issubset(set)
#set.issuperset(set)
#set.symmetric_difference(set)#returns left set after removed set of intersection
#set.symmetric_difference_update(set) #removes items present in both
a={'a','b','c'}
b={'c','d','e'}
c={'f','g','c'}
a.intersection_update(b,c)
print(a)
'''

'''
Dictionary : {key:value}
ordered
changeable/mutable
duplicates are not allowed
'''
a={
    1:'a',
    2:'b',
    3:'c',
    "apple":4
}
print(a)
print(len(a))
print(type(a))
print(a.keys())
print(a.values())
print(a.items())
print(a[1])
print(a.get("apple"))
a['apple']='white'
a['apple']='white'
print(a)
if "apple" in a:
    print("Yayy!!")
a.update({"green":2021})
print(a)
a.pop("apple")
print(a)
a.popitem()
print(a)
del a[1]
print(a)
#del a
#a.clear()
print(a)
for i in a:
    print(i)
for j in a:
    print(a[j])

for k in a.keys():
    print(k)
for l in a.values():
    print(l)
for s,t in a.items():
    print(s,t)
m=  a.copy()
print(m)

d=dict(a)
print(d)





    
