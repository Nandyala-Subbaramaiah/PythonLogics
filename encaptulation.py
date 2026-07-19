"""class Base: 
	def __init__(self): 
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"


class Derived(Base): 
	def __init__(self): 

		Base.__init__(self) 
		print("Calling private member of base class: ") 
		print(self.__c) 



obj1 = Base() 
print(obj1.a) 

class Employee:
    #private variable
 def __init__(self):
     self.__salary=0
     
class Dept(Employee):
    #setter 
 def set_salary(self,salary):
     self.__salary=salary
     #getter
 def get_salary(self):
     return self.__salary
d=Dept()
d.set_salary(50000)
print(d.get_salary())
"""
"""class A:
    __a=20
class B(A):
    def pr(self):
        print(self.__a)
        -+
b=B()
b.pr()"""

#private acces modifier
class A:
    def __init__(self):
        self.__name=''
class B(A):
    
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
        
b=B()
b.set_name("sai")
b.get_name()
print(b.get_name()) 


class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    # Getter for make
    @property
    def make(self):
        return self.__make

    # Setter for make
    @make.setter
    def make(self, value):
        self.__make = value

    # Getter for model
    @property
    def model(self):
        return self.__model

    # Setter for model
    @model.setter
    def model(self, value):
        self.__model = value
    
    # Getter for year
    @property
    def year(self):
        return self.__year

    # Setter for year
    @year.setter
    def year(self, value):
        self.__year = value

    def display_info(self):
        print(f"Car: {self.make} {self.model}, Year: {self.year}")

car = Car("Toyota", "Camry", 2020)
car.display_info() # Output: Car: Toyota Camry, Year: 2020

# Updating values using setters
car.make = "Honda"
car.model = "Accord"
car.year = 2021
car.display_info() # Output: Car: Honda Accord, Year: 2021

    
        
        
       