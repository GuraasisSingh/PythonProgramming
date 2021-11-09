#Session 32 HW
"""
#1. Class employee to store records of five employees.
class Employee:
    def __init__(self,name,doj,position,experience,salary):
        self.name=name
        self.doj=doj
        self.position=position
        self.experience=experience
        self.salary=salary
    def display(self):
        print(self.name, self.doj ,self.position, self.experience ,self.salary)
e1=Employee("Rohit","21st May,2014","Senior Manager","6 years", "10 LPA")
e2=Employee("Amit","3rd June,2016","Secretary","6 years", "15 LPA")
e3=Employee("Rahul","11th February,2018","Assistant Manager","3 years", "7 LPA")
e4=Employee("Mohan","10th July,2012","Vice President","9 years", "20 LPA")
e5=Employee("Sohan","31st May,2015","Assistant Vice President","7 years", "9 LPA")
e1.display()
e2.display()
e3.display()
e4.display()
e5.display()
"""
'''
#2. Class Animal and define various attributes to it
class Animal:
    cell="Multicellular"
    feed="Heterotrophic"
    state="Living"
    digestion="Alimentary Canal"
dog=Animal()
cow=Animal()
cat=Animal()
horse=Animal()
print(dog.cell)
print(cow.state)
print(cat.feed)
print(horse.digestion)
'''
'''
#3. Fruit class and define various attributes to it
class Fruit:
    edible="Pulp"
    non_edible="Seed"
    kind="Plant"
    colour="Yellow to green"
banana=Fruit()
mango=Fruit()
papaya=Fruit()
watermelon=Fruit()
print(banana.edible)
print(mango.non_edible)
print(papaya.kind)
print(watermelon.colour)
'''
'''
#4.Vegetable class and define various attributes to it
class Vegetable:
    edible="Whole"
    necessity="Health"
    kind="Plant"
capsicum=Vegetable()
bitter_gourd=Vegetable()
ladyfinger=Vegetable()
print(capsicum.edible)
print(bitter_gourd.necessity)
print(ladyfinger.kind)
'''
'''
#5.Department class and define attributes to it
class Department:
    name="Science"
    members="250"
    work="Research"
sc=Department()
print(sc.name)
print(sc.members)
print(sc.work)
'''
'''
#6.Student class and its objects
class Student:
    def __init__(self,name,dob,standard,rollno):
        self.name=name
        self.dob=dob
        self.standard=standard
        self.rollno=rollno
    def display(self):
        print(self.name, self.dob ,self.standard, self.rollno)
s1=Student("Amit","04/07/2012","Class 8",14563)
s2=Student("Mohan","08/01/2015","Class 6",13631)
s1.display()
s2.display()
'''
'''
#7. Citizen class and its objects
class Citizen:
    def __init__(self,name,dob,address):
        self.name=name
        self.dob=dob
        self.address=address
    def display(self):
        print(self.name, self.dob ,self.address)
c1=Citizen("Amit","04/07/2012","Chandigarh")
c2=Citizen("Mohan","08/01/2015","Delhi")
c1.display()
c2.display()
'''
'''
#8.Class School and define various attributes to it
class School:
    name="Xaviers"
    classrooms="50"
    teachers="150"
    rank=15
s1=School()
print(s1.name)
print(s1.classrooms)
print(s1.teachers)
print(s1.rank)
'''
