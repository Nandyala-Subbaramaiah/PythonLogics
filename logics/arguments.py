#positional orguments
def greet(name,age):
    print(f"{name} and {age}")
greet("subbu", 31)

#default orguments:
def greet(name,age=31):
    print(f"{name} and {age}")
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
    print(f"{name} and {age}")
greet()

#orbitary positional *args:
def sum_nums(*numbers):
    return sum(numbers)
print(sum_nums(10,20,30,40))

#orbitary positional orguments
def state_adress(**detail):
    for key,value in detail.items():
        print(f"{key}: {value}")
state_adress(name="tirupati", disrtict="tiruati", state="AP", village="kvp")
