#A class variable is shared across all instances of a class.
#It is defined inside the class but outside any instance methods.
class Car:
    #class level variable 
    wheel=4
    
    @classmethod
    def set_wheels(cls,new_wheels):
        cls.wheel=new_wheels
        
        
        
Car.set_wheels(6)
#Modifying Through the Class (Changes for All Instances)
#Car.wheel=6

car1=Car()
car2=Car()

#If modified using an instance, Python creates a new instance variable instead of modifying the class variable
#car1.wheel=7

print(car1.wheel)
print(car2.wheel)
print(Car.wheel)

"""5️⃣ Summary of Modifying Class Variables
Modification Method	Effect
ClassName.var = value	✅ Changes for all instances
instance.var = value	❌ Creates an instance variable (does NOT affect the class variable)
@classmethod	✅ Safely modifies class variables for all instances
@staticmethod	❌ Cannot modify class variables"""

#There are four primary ways to modify instance variables:
#Directly using dot notation: You can access the instance variable using the object's reference and the dot operator, then assign a new value to it.

#method1
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

my_car = Car("Red", "Sedan")
print(f"Original color: {my_car.color}")

my_car.color = "Blue"  # Modifying the instance variable
print(f"New color: {my_car.color}")


#method2
#Using setattr() function: Python's built-in setattr() function allows you to set the value of an attribute on an object.
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

my_car = Car("Red", "Sedan")
print(f"Original model: {my_car.model}")

setattr(my_car, "model", "SUV")  # Modifying the instance variable using setattr()
print(f"New model: {my_car.model}") 

#method3
#modify instance variables inside instance methods
class Person:
    def __init__(self,age):
        self.age=age
    
    def update_age(self, new_age):
        self.age=new_age

p=Person(24)
p.update_age(30)
print(p.age)

#method 4
#modify the instance variables using property setters(@property)
class Person1:
    def __init__(self, age):
        self.age=age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if value<0:
            raise ValueError("Age cann ot be negetive")
        self._age=value

p=Person1(35)
p.age=40
print(p.age) 