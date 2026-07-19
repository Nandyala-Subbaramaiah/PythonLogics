"""#Single Inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")
d=Dog()
d.bark()
d.speak()


#multilevel inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")
class ChildDog(Dog):
    def drink(self):
        print("drinking milk")
        
CHD=ChildDog()
CHD.speak()
CHD.bark()
CHD.drink()

#Multiple inheritance
class Calculation1:
     def sum(self,a,b):
         return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def division(self,a,b):
        return a/b;
    
der=Derived()
print(der.sum(10,20))
print(der.division(10,5))
print(der.Multiplication(2,3))


#Heiracle inheritance

class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("barking")
class Cat(Animal):
    def drink(self):
        print("drinking cat")

ct=Cat()
ct.eat()

ct.drink()

dg = Dog()
dg.eat()
dg.bark()
"""
"""#method overriding
class Animal:  
    def speak(self):  
        print("speaking")  
class Dog(Animal):  
    def speak(self):  
        print("Barking")  
d = Dog()  
d.speak() 


#super keyword
class A:
    def __init__(self):
        print("constructor")
class B(A):
    def __init__(self):
        super().__init__()

b=B()
 
class A:
    def method(self):
        print("mothod A")
class B(A):
    def method(self):
        print("method B")
class C(A):
    def method(self):
        print("method C")
class D(B,C):
    pass
        
d=D()
d.method()
     
from abc import ABC, abstractmethod

# Base class
class Vehicle(ABC):  # Inherits from ABC to enforce abstract methods
    def __init__(self, fuel_efficiency):
        self.fuel_efficiency = fuel_efficiency  # Fuel efficiency in miles per gallon
    
    @abstractmethod
    def calculate_range(self):  # Abstract method to enforce implementation in subclasses
        pass

# Subclass for Car
class Car(Vehicle):
    def __init__(self, fuel_efficiency, tank_capacity):
        super().__init__(fuel_efficiency)
        self.tank_capacity = tank_capacity  # Tank capacity in gallons

    def calculate_range(self):
        return self.fuel_efficiency * self.tank_capacity  # Range = Efficiency × Capacity

# Subclass for Truck
class Truck(Vehicle):
    def __init__(self, fuel_efficiency, tank_capacity, load_weight):
        super().__init__(fuel_efficiency)
        self.tank_capacity = tank_capacity  # Tank capacity in gallons
        self.load_weight = load_weight  # Load weight in tons

    def calculate_range(self):
        # Assuming range decreases by 5 miles per ton of load weight
        base_range = self.fuel_efficiency * self.tank_capacity
        return base_range - (5 * self.load_weight)

# Subclass for Motorbike
class Motorbike(Vehicle):
    def __init__(self, fuel_efficiency, tank_capacity, engine_type):
        super().__init__(fuel_efficiency)
        self.tank_capacity = tank_capacity  # Tank capacity in gallons
        self.engine_type = engine_type  # Engine type (e.g., "single-cylinder", "multi-cylinder")

    def calculate_range(self):
        # Assuming single-cylinder engines have 10% higher range
        base_range = self.fuel_efficiency * self.tank_capacity
        if self.engine_type == "single-cylinder":
            return base_range * 1.1
        return base_range

# Example usage
if __name__ == "__main__":
    car = Car(fuel_efficiency=30, tank_capacity=15)
    print(f"Car range: {car.calculate_range()} miles")

    truck = Truck(fuel_efficiency=15, tank_capacity=20, load_weight=3)
    print(f"Truck range: {truck.calculate_range()} miles")

    motorbike = Motorbike(fuel_efficiency=50, tank_capacity=4, engine_type="single-cylinder")
    print(f"Motorbike range: {motorbike.calculate_range()} miles")
    """

