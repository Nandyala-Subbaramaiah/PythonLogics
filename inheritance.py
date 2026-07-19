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
"""

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

"""#method overriding
class Animal:  
    def speak(self):  
        print("speaking")  
class Dog(Animal):  
    def speak(self):  
        print("Barking")  
d = Dog()  
d.speak() """


"""#super keyword
class A:
    def __init__(self):
        print("constructor")
class B(A):
    def __init__(self):
        super().__init__()

b=B()"""
      

    