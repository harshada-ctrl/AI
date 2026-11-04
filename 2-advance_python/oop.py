# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 20:01:20 2026

@author: Admin
"""
class Circle:
    def __init__(self, x,y,r):
        self.x=x
        self.y=y
        self.r=r
        
    def circumference(self):
        return 2*3.14* self.r
    def area(self):
        return 3.14 *self.r * self.r
    
    
#creating an object of circle    
a_circle= Circle(2.0, 2.0, 1.0)
b_circle= Circle(2.0, 3.0, 1.0)
    
#Accessing data and methods of b_circle
print("redius:", a_circle.r)
print("circumference:", a_circle.circumference())
print("Area:", a_circle.area())


#24 july 2026 no class


#25 july 2026 
 #encapsulation
'''hiding inteernal data by making attributes 
private and exposing theam via methods'''
   
class Circle:
    def __init__(self, x, y, r):
        self.__x = x
        self.__y = y
        self.__r = r
        
    def get_radius(self):
        return self.__r
    
    def set_radius(self, r):
        if r > 0:
            self.__r = r
        else:
            print("invalid radius")
            
#usage
c2 = Circle(1,2,3)
print(c2.get_radius())
c2.set_radius(10)
#data is protected; direct acess is avoided
print(c2.get_radius())

#base class
class Circle:
    def __init__(self, x, y, r):
        self.__x = x
        self.__y = y
        self.__r = r
    
    def area(self):
        return 3.14 * self.r ** 2
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
    def display_info(self):
        print(f"Center: ({self.x}, {self.y},Radius: {self.r})")
        print(f"Area: {self.area():.2f}")
        print(f"Circumference: {self.circumference():.2f}")

#derived class
class ColoredCircle(Circle):
    def __init__(self, x, y, r, color):
        super().__init__(x, y, r)
        self.color = color

#overriding the display_info method        
    def display_info(self):
         super().display_info()
         print(f"Color: {self.color}")
         
#usage
c1 = ColoredCircle(0, 0, 5, "red")
c1.display_info()
         

 '''
 Polymorphism is one of the core concepts of
Object-Oriented Programming (OOP), and it refers
to the ability of different objects to respond in
their own way to the same method or function call.
The word "polymorphism" comes from Greek:
poly = many, morph = form
So, polymorphism means "many forms
Types of Polymorphism in Programming:
1. Compile- Time Polymorphism (Static Binding)
Also known as method overloading.
Same method name with different parameters.
Decision is made at compile time.''' 

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
    
calc = Calculator()
print(calc.add(5))
print(calc.add(5, 3))
print(calc.add(5, 3, 2))

'''Run- Time Polymorphism (Dynamic Binding)
Also known as method overriding.
A chi Ld class overrides a method of its parent class.
Decision is made at runtime.'''
#method overriding
class Animal:
    def speak(self):
        print("Animal speaks")
        
class Dog(Animal):
    def speak(self):
        print("Dog barks ")
        
class Cat (Animal):
    def speak(seLf):
        print("Cat meows")

#polymorphism in action
for animal in [Dog(), Cat()]:
    animal.speak()
      
        

        
        
##another example

class Circle:
    def area(self):
        return "calculating area of circle"
        
class Square:
    def area(self):
        return "calculating area of square"
        

#usage
shapes = [Circle(), Square()]
for shape in shapes:
    print(shape.area())



'''Abstraction is another fundamental concept in
Object-Oriented Programming (OOP) .
It refers to the process of hiding the
complex implementation details and showing only
the essential features of an object or system
When you drive a car, you use the steering wheel,
brake, and accelerator, but you don 't need to know
how the engine works internally.
That's abstraction — you interact
with a simplified interface.
Abstraction helps in designing clean and
simple interfaces while hiding internal code complexity.
In Python, abstraction is implemented using:
Abstract Classes
interfaces (via abstract base classes)

'''

from abc import ABC, abstractmethod

#abstract method
class Vehicle(ABC):
    
    @abstractmethod 
    def start(self):
        pass
    
    @abstractmethod 
    def stop(self):
        pass
    
# Concrete class
class Car(Vehicle):
    def start(self):
        print( "Car started")
    def stop(self):
        print( "Car stopped")
        
# usage
v = Car()
v. start()
v. stop()
   


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area (self):
        return 3.14 * self.r ** 2
# Usage
c4 = Circle(4)
print( "Area: " , c4.area())










        
    
    
    
    
    
    
    
    