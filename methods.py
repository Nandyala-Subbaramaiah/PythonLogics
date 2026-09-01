"""class Dog:
    def __init__(self,name):
        self.name=name
        
    def bark(self): #instance method
        print(f"{self.name} says woof!")
    
dog=Dog("Chitti")
dog.bark()

#classmethods
class Dog:
    species='canine'
    @classmethod
    def set_species(cls,species):
        cls.species=species
    def __init__(self,name):
        self.name=name
        
dog=Dog("richchi")
Dog.set_species("wolf")
print(Dog.species)


#staticmethod
class Dog:
    @staticmethod
    def bark():
        print("woof woof!")
Dog.bark()
"""
# //////////////////////////////////// class methods, static methods, instance methods ////////////////////////
class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod # class methods take cls as the first parameter, allowing them to access class variables and methods.
    def class_method(cls):
        cls.class_variable = "Class variable modified by class method"
        return f"Class method called. Accessing: {cls.class_variable}"

    @staticmethod # static method doesn't take self or cls as the first parameter, so it cannot access instance or class variables directly.
    def static_method():
        return "Static method called. No access to class or instance variables."

    def instance_method(self): # instance methods take self as the first parameter, allowing them to access instance variables and methods.
        return f"Instance method called. Accessing: {self.instance_variable}"

my_instance = MyClass("I am an instance variable")
print(my_instance.class_method())  # Accessing class method and modifying class variable
print(MyClass.class_method())  # Accessing class method without instance and modifying class variable
print(my_instance.static_method())  # Accessing static method
print(MyClass.static_method())  # Accessing static method without instance
my_instance.instance_variable = "Modified instance variable"
print(my_instance.instance_method())  # Accessing instance method