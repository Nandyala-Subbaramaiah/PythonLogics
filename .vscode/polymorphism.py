"""
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
def func(obj): 
        obj.capital()
        obj.language()
        obj.type()
        
obj_india=India()
obj_usa=USA()
    
func(obj_india)
func(obj_usa)
"""   
class Animal:
    def speak(self):
        raise NotImplementedError("subclass must implement this method")
class Dog(Animal):
    def speak(self):
        return "woof"
class Cat(Animal):
    def speak(self):
        return "Meo"
    
animals=[Dog(), Cat()]
    
for animal in animals:
        print(animal.speak())  