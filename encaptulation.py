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



    
        
        
       