'''
Principles:
> Data Abstraction

from abc import XYZ
class Car(XYZ):
    def mileage(self):
        pass
> Polymorphism

#len is poly morphic
print(len("GURAASIS"))
print(len([10,30,50]))

> Inheritance-reusability of code

parent/base class
derived/child class
class Animal:
    def speak(self):
        print("Animal Speaking:")
#child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("Dog barking")
d=Dog()
d.bark()
d.speak()

> Encapsulation

eg-class
_ protected
__ private
'''
