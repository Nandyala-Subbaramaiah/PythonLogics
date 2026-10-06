#positional orguments
import numbers


def greet(name,age):
    print(f"positional args:{name} and {age}")
greet("subbu", 31)

#default orguments:
def greet(name, age=31):
    print(f"default args: {name} and {age}")
greet("subbu")
#rules for default orgs
########rule 1##########
#none-default paramaters must come befor default parameters in the function definition.
#position arguments must come before keyword arguments when calling a function.
#using keyword orguments order does not a matter 
#each paramter must have only one value
#keyword name must match exactly function definition
#for positional order matter strictly


#keyword orguments:
def greet(name="subbu",age=31):
    print(f"keyword args: {name} and {age}")
greet()

#orbitary positional *args:
def sum_nums(*numbers):
    print(f"args: {numbers}")
    return sum(numbers)

print(sum_nums(10,20,30,40))

#orbitary positional orguments **kwargs:
def state_adress(**detail):
    for key,value in detail.items():
        print(f"{key}: {value}")
    print(f"keyword args: {detail}")
state_adress(name="tirupati", disrtict="tiruati", state="AP", village="kvp")


#What is the order of arguments in a Python function?

# The typical order is:

# Positional parameters

# *args

# Keyword-only parameters

# **kwargs

def example(a, b=10, *args, c=20, **kwargs):
    print(a, b, args, c, kwargs)

example(1, 2, 3, 4, c=5, d=6)