#Session 34
from collections import Counter
#collection provide general sequences and variables required for lists, tuples, sets and dictionaries
print(Counter(['B','A','C','B','A','C']))
print(Counter({'A':2,'B':3,'C':2,}))
print(Counter(A=2,B=3,C=2))
'''
Inheritance:

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
        
class Student(Person):
    def __init__(self,fname,lname,year):
        #add the properties
        #Person.__init__(self,fname,lname)[can also be used]
        super().__init__(fname,lname)#no need to use the self here.
        self.graduationyear=year
    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the Class",self.graduationyear)
x=Person("Guraasis","Singh")
x.printname()

y=Student("Guraasis","Singh",2021)
y.printname()
print(y.graduationyear)
y.welcome()
#Anagrams
a=(1,5,2,11,8)
b=sorted(a)
print(b)
g=sorted(a,reverse=True)
print(g)
#----------------------------------
n1=input("Enter number 1\n")
n2=input("Enter number 2\n")
if sorted(n1)==sorted(n2):
    print("Anagrams")
else:
    print("Not Anagrams")
#----------------------------------
def check(s1,s2):
    if (Counter(s1)==Counter(s2)):
        print("ANAGRAMS")
    else:
        print("NOT ANAGRAMS")
s1=input("Enter the string 1:\n")
s2=input("Enter the string 2:\n")
check(s1,s2)
#----------------------------------

'''

