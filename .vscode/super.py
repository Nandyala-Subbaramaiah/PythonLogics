#super() functon is used to call the parent class constructor and methods. 
# It allows you to access the methods and properties of a parent class from a child class. 
# This is particularly useful in inheritance, where a child class can extend or override the functionality of its parent class.
class A:
    def __init__(self,name):
        self.name=name
        print(f"{name} sense less fellow")
        
class B(A):
    def consult_doctor(self, name):
        print(f"before super: {id(self)} | current self: {self.name}")
        super().__init__(name) # object state is updated with the new name value, but the id of the object remains the same(creates only one object).
        print(f"before super: {id(self)} | updated self: {self.name}")
        print(f"{name} doctor provide treatment")
        print(f"name for doctor : {self.name}")

bhv=B("rani")
print({id(bhv)})
print({id(bhv.consult_doctor("subbu"))})