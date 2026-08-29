"""#lists
test_list=[2,4,1,10]
#tupels adding single list
test_tup=(12,20,21)
#test_list+=test_tup
#test_list.extend(list(test_tup))
list_with_tuple = list(sum(zip(test_list, test_tup), ()))
print("test_tuples:", (list_with_tuple))
#we can accessing the tuple elements using indeces
fruits=("mango","bannana","apple")
print(fruits[1])
vegetables = ("carrot", "potato")
combined=fruits+vegetables
print(combined)
print(fruits[0:2])

numbers = (1, 2, 3, 4, 5)
print(len(numbers))   # Output: 5
print(max(numbers))   # Output: 5
print(min(numbers))   # Output: 1
"""
 
# Creating a dictionary with tuples as keys
locations = {
    (10.0, 20.0): "Park",
    (30.0, 40.0): "Museum",
    (50.0, 60.0): "Library"
}

# Accessing a value using a tuple key
print(locations[(10.0, 20.0)])  # Output: Park
# Creating a set of tuples
unique_coordinates = set()
unique_coordinates.add((10.0, 20.0))
unique_coordinates.add((30.0, 40.0))
unique_coordinates.add((10.0, 20.0))  # Duplicate, won't be added

# Printing the set
print(unique_coordinates)  # Output: {(10.0, 20.0), (30.0, 40.0)}



#it converts from the multiple lists to one single lists of mulple dictionaries 
list1 = [1, 2, 3] 
list2 = ['a', 'b', 'c'] 
list3 = ['x', 'y', 'z']

zipped=zip(list1,list2,list3)
zipped_list=list(zipped)
print(zipped_list)  

