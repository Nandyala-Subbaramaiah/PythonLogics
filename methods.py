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
