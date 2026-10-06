"""Counting occurrences
Grouping using dictionaries
Nested dictionaries
List of tuples → nested dictionary
List of dictionaries → dictionary indexed by ID
Dictionary comprehension 
Sorting dictionaries
Finding max/min
Merging dictionaries
get() vs setdefault()
Dictionary internal implementation / hash table
Dictionary time complexity
Nested JSON transformation
Flattening nested dictionaries
Real API response transformation"""

"""#finding max value and duplicates in dictionary
ini_dict = {'a':1, 'b':2, 'c':3, 'd':2}
new_dict={}
x=ini_dict.get('a')
for key, value in ini_dict.items():
    if value>x:
        x=value
        y=key
print(y,":",x)        
if value not in new_dict.values():
        new_dict[key]=value
print(new_dict)

#finding minimum value here
ini_dict = {'a':1, 'b':2, 'c':3, 'd':2}
x=ini_dict.get('c')
for key,value in ini_dict.items():
    if value<x:
        x=value
        y=key
print(y,x)

#another method
Tv={"Evildead":100,"Terminator":1200,"GameOfThrowns":70}
keymax=min(zip(Tv.values(),Tv.keys()))[0]
print(keymax)


# Python3 code to demonstrate working of
# Max / Min of tuple dictionary values
# Using tuple() + min()/max() + zip() + values()

# Initializing dictionary
test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3, 2), 'best' : (1, 4, 9)}
#res = tuple(max(x) for x in zip(*test_dict.values()))

# printing result
 
res=tuple(map(min,*test_dict.values()))
print("The maximum values from each index is : " + str(res))


#The pop() method in a dictionary removes and returns an element specified by a key. When you use the pop() method, it will take the specified key, remove the key-value pair associated with that key from the dictionary, and return the value.
Dict1={1:'subbu',2:'ramana',3:'rama'}
pop_key=Dict1.pop(1)
print(Dict1)


Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}        
for x in Employee.items():        
    print(x)    
  
keys=[1,2,3,4,50]
values=['a','b','c','d','e']
newdict=dict(zip(keys,values))
print(newdict)
 

 
# Output: {'a': 1, 'b': 5, 'c': 4}



dict1={1:'a',6:'b',5:'c'}
dict2={1:'a',6:'b',5:'c'}
for key,value in dict1.items():
    if dict1==dict2:
        print("print equals")
        break
    else:
        print("not equals")
        break

dict1={'subbu':1,'rama':3}
#x=dict1['rama']
#x=dict1.get('subbu')
#x=dict1.keys()
#x=dict1.values()
dict1["color"] = "white"

x=dict1.items()
dict1["year"] = 2020
print(x)
 
 
 #Convert Key-Value list Dictionary to List of Lists
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
res=[]
#for key,value in test_dict.items():
 #res.append([key]+value)
#res=[[key]+value for key,value in test_dict.items()]
                   
#5: Using zip() function and list comprehension
res=[[key]+value for key,value in zip(test_dict.keys(), test_dict.values())]
print(res)





#tuple data ande list of lists converts to dictionaries
data = [["a", 1], ["b", 2], ["c", 3]]

#data=[("a",10),("b",20),("c",8)]
dict_comprehension={key:value for key,value in data}
print(dict_comprehension)



#convert list to dictionary
list1=['a','b','c']
list2=[1,2,3]
newdict=dict(zip(list1,list2))
print(newdict)

#converts two saparate list
data={'a': 1, 'b': 2, 'c': 3}
key_list=list(data.keys())
value_list=list(data.values())
print(key_list)
print(value_list)




#Convert Key-Value list Dictionary to List of Lists
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
#for key,value in test_dict.items():
    #res.append([key]+value) 
    #res=[[key]+value for key,value in test_dict.items()]
                   
#5: Using zip() function and list comprehension
res=[[key]+value for key,value in zip(test_dict.keys(), test_dict.values())]
print(res)
 



def find_countries_for_places(countries_dict, places_list):
    
    return {place:country for country, cities in countries_dict.items() for place in places_list if place in cities}

# Example dictionary of countries and cities
countries_data = {
    "USA": ["New York", "Los Angeles", "Chicago"],
    "India": ["Mumbai", "Delhi", "Bangalore"],
    "UK": ["London", "Manchester", "Liverpool"],
    "France": ["Paris", "Lyon", "Marseille"]
}

# Example list of places (cities)
places = ["Mumbai", "Chicago", "Paris", "Liverpool"]

# Get country for each place
result = find_countries_for_places(countries_data, places)

# Print result
print(result)

#converting data based on the first character of the word
grouped={}
for word in result:
    first_char=word[0]
    if first_char not in grouped:
        grouped[first_char]=[]
    grouped[first_char].append(word)

#converting to jason formate
import json
json_data = json.dumps(grouped)
print("jason formate:",json_data)

def sum_dict_values(d):
    total = 0
    for v in d.values():
        if isinstance(v, dict):
            total += sum_dict_values(v)
        else:
            total += v
    return total

data = {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
print(sum_dict_values(data))  # ➤ 6

#convert the list of tuples to dictionary with nested structure and occorances count for users
data = [
    ("user1", "name", "John"),
    ("user1", "age", 25),
    ("user2", "name", "Alice"),
    ("user2", "age", 30)
]

result = {}

for user,key,value in data:
    if user not in result:
        result[user]={"occorances":0}
    result[user][key] = value   
    result[user]["occorances"]+=1
print(result)


#convertig jjson formate to dictionary with nested structure
users=[
    {
        "user_id": "user1",
        "name": "John",
        "age": 25,
        "city": "Chennai"
    },
    {
        "user_id": "user2",
        "name": "Alice",
        "age": 30,
        "city": "Bangalore"
    },
    {
        "user_id": "user3",
        "name": "David",
        "age": 28,
        "city": "Hyderabad"
    }
]

res={}

for user in users:
    user_id = user["user_id"]
    res[user_id] = {
        "name":user["name"],
        "age":user["age"],
        "city":user['city']
    }
print(res)

#grouped
words = ["apple", "ant", "ball", "bat", "cat"]

grouped = {}

for word in words:
    first_letter = word[0]

    if first_letter not in grouped:
        grouped[first_letter] = []

    grouped[first_letter].append(word)

print(grouped)


students = [
    ("John", "IT"),
    ("Alice", "HR"),
    ("Bob", "IT"),
    ("David", "HR")
]


grouped_students = {}

for name,department in students:
    if department not in grouped_students:
        grouped_students[department]=[]
    grouped_students[department].append(name)

print(grouped_students)


numbers = [1, 2, 3, 4, 5, 6]

grouped = {
    "even": [],
    "odd": []
}


for number in numbers:
    if number % 2 == 0:
        grouped["even"].append(number)
    else:
        grouped["odd"].append(number)

print(grouped)


words = ["cat", "dog", "apple", "bat", "orange"]

grouped = {}

for word in words:
    length = len(word)

    if length not in grouped:
        grouped[length] = []

    grouped[length].append(word)

print(grouped)


transactions = [
    ("John", 100),
    ("Alice", 200),
    ("John", 150)
]

grouped={}

for name,amount in transactions:
    if name not in grouped:
        grouped[name]=[]
    grouped[name].append(amount)
print(grouped)


employees = [
    {"name": "John", "city": "Chennai"},
    {"name": "Alice", "city": "Bangalore"},
    {"name": "Bob", "city": "Chennai"}
]

grouped={}

for employee in employees:
    city = employee["city"]
    name = employee["name"]

    if city not in grouped:
        grouped[city] = []

    grouped[city].append(name)

print(grouped)


# Nested dictionaries
student_records = {
    "student1": {
        "name": "John",
        "marks": {"math": 90, "science": 85}
    },
    "student2": {
        "name": "Alice",
        "marks": {"math": 95, "science": 92}
    }
}

# Access and update a value in the innermost dictionary
print(student_records["student1"]["marks"]["math"])
student_records["student1"]["marks"]["math"] = 96

# Iterate through the nested dictionaries
for student_id, student in student_records.items():
    print(student_id, student["name"], student["marks"])

"""
# Dictionary comprehension problems
# 1. Map each number from 1 to 5 to its cubes
cubes = {number: number ** 3 for number in range(1, 6)}
print(cubes)

# 2. Keep only even numbers and map each to its square
numbers_to_check = [1, 2, 3, 4, 5, 6]
even_squares = {
    number: number ** 2
    for number in numbers_to_check
    if number % 2 == 0
}
print(even_squares)

# 3. Map each word to its length, keeping words longer than three characters
words_to_check = ["cat", "apple", "banana", "dog"]
long_word_lengths = {
    word: len(word)
    for word in words_to_check
    if len(word) > 3
}
print(long_word_lengths)

# 4. Swap keys and values; original values should be unique
scores = {"Alice": 90, "Bob": 85, "Chris": 92}
scores_by_points = {score: name for name, score in scores.items()}
print(scores_by_points) 