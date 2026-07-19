# A simple Python function
'''
def function():
    print("Welcome to GFG")


# Driver code to call a function
function()

def add(num1:int,num2:int )-> int:
    num3=num1+num2
    
    return num3
num1,num2=10,20
ans=add(num1,num2)
print(f"The addition of {num1} and {num2} results {ans}.")

def evenOdd(x):
    if(x % 2 == 0):
        print("even")
    else:
        print('odd')
evenOdd(2)
evenOdd(3)  
     
    #default orgumrnt     
def myFun(x, y=10):
    print("x",x)
    print('y',y)
    
myFun(20)

    #parameter orgument
def student(first_name,last_name):
    print(first_name,last_name)
    
student(first_name='Geeks', last_name='Practiese')
student(last_name='Subbu', first_name='Nandyala')
#positional parameters
def nameAge(name,age):
    print("Hi, I am", name)
    print("My age is", age)
print("case-1")    
nameAge("subbu",29)
print("\ncase-2:")
nameAge(29,"subbu")    

#Arbitary keyword arguments

def myFun(*args):
    for arg in args:
        print(arg)
        
myFun('Hello','Welcome','GeeksFoeGeeks')


def myFunn(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
        
myFunn(first='Geeks', mid='for', last='nandyala')
'''
# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
    s = 'I love GeeksforGeeks'
    
    def f2():
        print(s)
        
    f2()
    f1()

             

# Python code to illustrate the cube of a number
# using lambda function
def cube(x): 
 return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))

#return statement in python
def square(num):
    
    return num**2

print(square(2))

#pass by value pass by references

def myFun(x):
    x[0]=20
    
list=[12,11,13,14,15]
    
myFun(list)

print(list)
    