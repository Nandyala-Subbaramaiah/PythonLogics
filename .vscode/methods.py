#instance methods
class Car:
    def __init__(self,color):
        self.color=color
    
    def repaint(self,new_color):
        self.color=new_color

my_car=Car("red")
print(my_car.color)
my_car.repaint("blue")
print(my_car.color)

#class methods
class Dog:
    species="canis familiaris"
    
    @classmethod
    def set_species(cls,species):
        cls.species=species

    def __init__(self,name):
        self.name=name
        print(f"Dog {self.name} is a {self.species}")
        
dog=Dog("rexona")
Dog.set_species("wolf")
print(Dog.species)

#static methods
class Dog:
    @staticmethod
    def bark():
        print("woof woof")

Dog.bark()

