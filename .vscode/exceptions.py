"""class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def risky_function(value):
    if value < 0:
        raise CustomError("Value cannot be negative")
    return value * 2

try:
    result = risky_function(-5)
    print(result)
except CustomError as e:
    print(f"Caught an exception: {e.message}")


#zero division error 
a = 10
b = 0

try:
    result = a / b
    print("connot devisible by zero")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("print the necessary code of the program")
    
#index errors
my_list = [1, 2, 3]
  
try:
    print(my_list[3])
except IndexError:
    print("indexing error")
finally:
    print("print the necessary code of the program")
    
my_dict = {"name": "Alice", "age": 30}

# This will raise a KeyError because the key 'address' does not exist in the dictionary
try:
    address = my_dict["address"]
except KeyError:
    print("Error: Key not found in the dictionary.")

#custom exception
class CustomError(Exception):
    def __init__(self, message):
        self.message=message
        super().__init__(self.message)#calls the parent class (Exception) initializer with the message.
def risky_function(value):
    if value<0:
        raise CustomError("value cannot be negetive")
    return value*2
try:
    result=risky_function(-5)
    print(result)
except CustomError as e:
    print(f"cought an exception:{e.message}")

class CustomAgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 0 or age > 120:
        raise CustomAgeError(age)
    elif age < 18:
        print(f"Age {age} is valid, but you are not eligible to vote.")
    else:
        print(f"Age {age} is valid. You are eligible to vote.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except CustomAgeError as e:
    print(f"CustomAgeError: {e.message}. Provided age: {e.age}")
except ValueError:
    print("Invalid input. Please enter a number.")

"""

class CustomeAgeError(Exception):
    def __init__(self,age,message="age must be 0 to between 120"):
        self.age=age
        self.message=message
        super().__init__(self.message)

def check_age(age):
    if age<0 or age>120:
        raise CustomeAgeError(age)
    elif age<18:
        print(f"age {age} is valid, your not eligible for vote")
    else:
        print(f"age{age}is valid, your eligible for vote")
        
try:
    age=int(input("Enter your age "))
    check_age(age)
except CustomeAgeError as e:
    print(f"cought an exception {e.message}.Provided age {e.age} ")
except ValueError:
    print("invalid input, please enter a value")
        