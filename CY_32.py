#Session 32 
'''
OOPs:
>Classes
>Object

class Dog:
    name="Tommy"
d=Dog()
print(d.name)

__init__  ->(constructor)-called when object is created.

method is that function which is dependent on the object.
functions are independent of objects

self ->Its a parameter access attributes

class Car:
    def __init__(self,modelname,year):#parameters
        self.modelname=modelname
        self.year=year
    def display(self):
        print(self.modelname,self.year)
c1=Car("Suzuki",2021)#arguments
c1.display()

class Car:
    def __init__(a,modelname,year):#parameters
        a.modelname=modelname
        a.year=year
    def display(a):
        print(a.modelname,a.year)
        
c1=Car("Suzuki",2021)#arguments
c1.display()

METHOD :
> called by its name (can or cannot)
> associated /dependent on the objects
> implicitly passes  on the object on which it is invoked
> may or may not return any data
> a method can operate on the data (object's variable) that is contained by the corresponding class

#user defined method
class Abc:
    def a(self):
        print("This is method")
obj=Abc()
obj.a()

#in built method
import math
c=math.ceil(14.23)
print("Ceil value",c)


FUNCTION:
> can be ONLY called by its name
> block of code that is also been by its name
> independent of object
> may or may not have parameters
  if any parameter is going to be passed, they are explicitly passed.
> may or may not return any data
> FUNCTION does not deal with the class and its objects concept.

#user defined function
def sub(a,b):
    return a-b
print("Subtraction:",sub(10,4))


# in built function
s=sum([2,5])
print(s)
h=max(2,5)
print(h)

'''
