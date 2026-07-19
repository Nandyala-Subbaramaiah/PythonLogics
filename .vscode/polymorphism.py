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
        
"""   

class A:
    def product(self, a, b):
        p = a * b
        print(p)

class B(A):
    def product(self, a, b, c):
        p = a * b * c
        print(p)

b = B()
# This line will call the overridden product method in class B
b.product(4, 5,5)

# To call the product method in class A, you can use super()
# Uncomment the following lines if you want to see the output of the A class method
# a = A()
# a.product(4, 5)



"""#method overriding 
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

print("Dog sound: ", dog.sound())
print("Cat sound: ", cat.sound())
class A:
    
    def add(self,a,b):
        return a+b
class B(A):
    def add(self,a,b,c):
         a=b+c
b=B()
print(b.add(1,2,3))


class MathUtils:
    def add(self, a, b, c=0):
        return a + b + c

# Create an instance of MathUtils
utils = MathUtils()

print("Sum of two integers: ", utils.add(10, 20))
print("Sum of three integers: ", utils.add(10, 20, 30))


class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

print("Dog sound: ", dog.sound())
print("Cat sound: ", cat.sound())
"""
class Math:
    def add(self, *args):
        return sum(args)
math=Math()
print(math.add(10,20))
print(math.add(10,20,30))
