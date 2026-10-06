"""class MathOperations:
    pi=3.2324
    @classmethod
    def area_of_circle(cls,radius):
        return cls.pi*(radius **2)
print(MathOperations.pi)
print(MathOperations.area_of_circle(5)) 

# static class 
# demonstrate static methods 
class Maths(): 
	
	@staticmethod
	def addNum(num1, num2): 
		return num1 + num2 
		

	# Calling method of class 
	# without creating instance 
# res = Maths.addNum(1, 2) #calling through the object refference
print("The result is", Maths.addNum(10,20)) #using class name also called the method

from abc import ABC, abstractmethod

class Animal(ABC):
	@abstractmethod
	def animal_type(self):
		pass

class Dog(Animal):
	def animal_type(self):
		print("Dog is a domestic animal")

class Cat(Dog):
	def animal_type(self):
		super().animal_type()
		print("shouting meo")

# c=Animal() #we can't create abstract object, just it helps to declare method 
# c.animal_type()
ct=Cat()
ct.animal_type()

	
#dataclases

from dataclasses import dataclass
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

student = Student("John", 25)

print(student.name)# Python automatically creates the constructor, so you can directly do:
print(student.age)


#singletone class
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls) #this part calling the object for the first time created.

        return cls._instance #this part returning the existing object only instead create new one.


db1 = Database()
db2 = Database()

print("singleton", db1 is db2)


#metaclasess
# 1. Create the Metaclass
class EnforceCapitalization(type):
    def __new__(cls, name, bases, dct):
        # Check if the class name starts with a lowercase letter
        if name[0].islower():
            raise TypeError(f"Class name '{name}' must start with an uppercase letter!")
        
        # If valid, create the class normally
        return super().__new__(cls, name, bases, dct)

# 2. This works perfectly
class ValidName(metaclass=EnforceCapitalization):
    pass

# 3. This will instantly raise a TypeError
class invalidName(metaclass=EnforceCapitalization):
    pass"""

# RULES:METACLASESS
# The __new__ and __init__ methods must accept four specific arguments in order:
# cls / mcs: The metaclass itself.
# name: The name of the class being created (string).
# bases: A tuple of parent classes the class inherits from.
# dct / namespace: A dictionary containing the class variables and methods.


# normal classes for student creation

class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}")

students={}

def add_student(student_id, name, age):
    student = Student(student_id, name, age) 
    students[student_id] = student

add_student(1, "Alice", 20)
add_student(2, "Bob", 22)
add_student(3, "Charlie", 19)

for student_id, student in students.items():
    student.display_info()
