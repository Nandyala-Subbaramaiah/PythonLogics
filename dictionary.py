#finding max value and duplicates in dictionary
"""ini_dict = {'a':1, 'b':2, 'c':3, 'd':2}
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
"""


# Python3 code to demonstrate working of
# Max / Min of tuple dictionary values
# Using tuple() + min()/max() + zip() + values()

# Initializing dictionary
"""test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3, 2), 'best' : (1, 4, 9)}
#res = tuple(max(x) for x in zip(*test_dict.values()))
# printing result
res=tuple(map(min,*test_dict.values()))
print("The maximum values from each index is : " + str(res))



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
 


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# Example usage
dict1={1:'a',2:'b',3:'c'}
dict2={4:'a',5:'z',6:'f'}
print(merge_dicts(dict1, dict2))
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





#tuple data ande list of lists
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

"""
