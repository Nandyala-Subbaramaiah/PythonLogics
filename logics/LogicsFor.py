'''#swap first and last number 
def swaplastfirst(newList):
    size=len(newList)
    
    temp=newList[0]
    newList[0]=newList[size-1]
    newList[size-1]=temp
    
    return newList
    
newList=[1,2,3,4,5]
    
print(swaplastfirst(newList))

def swapfirstlast(newList):
    newList[0],newList[-1]=newList[-1],newList[0]
    return newList
newList=[10,20,40,50]
print(swapfirstlast(newList))

def swap(list):
    get=list[-1],list[0]
    list[0],list[-1]=get
    return list
    
list=[23,34,23,11]
print(swap(list))

def swaplist(list):
    
    first=list.pop(0)
    last=list.pop(-1)
    
    list.insert(0,last)
    list.insert(-1,first)
    
    return list

list=[23,34,56,67,88]
print(swaplist(list))

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2]=list[pos2], list[pos1]
    return list
list=[23,11,34,56,78]
pos1, pos2=1,2
print(swapPositions(list,pos1-1, pos2-1))

def swap(list, pos1, pos2):
    #poping both the elements from list
     first_ele=list.pop(pos1)
     second_ele=list.pop(pos2-1)
    #inserting in each others positions 
     list.insert(pos1, second_ele)
     list.insert(pos2, first_ele)
     return list

list=[45,56,23,556,1]
pos1,pos2=1,4
print(swap(list,pos1-1,pos2-1))

def swap(list,pos1,pos2):
    get=list[pos1], list[pos2]
    list[pos2],list[pos1]=get
    return list
list=[12,34,56,78,8]
pos1,pos2=1,3
print(swap(list,pos1-1,pos2-1))

def swap(list,pos1,pos2):
    temp=list[pos1]
    list[pos1]=list[pos2]
    list[pos2]=temp
    return list
list=[23,4,6,7,8,7]
pos1,pos2=1,3
print(swap(list,pos1-1,pos2-1))
#Remove duplicate from list


#Removed duplicates using 
list = [1,1,3,4,5,5,5,6]

for i in range(len(list)):
    for k in range(len(list)):
        if i == k :#find duplicates first
            continue
        elif list[i] == list[k]:
            del list[k]#deleted duplicate elements
            list.append("0")
          

print(list)
list = [item for item in list if item != '0']
print(list)

# initializing list
"""list1 = [1, 5, 3, 6, 3, 5, 6, 1]
list1 = list(set(list1))
print ((list1))"""

#maximum number
def max(a,b):
    if a>=b:
      return a
    else:
       return b
a=10
b=30
print(max(a,b))

#maxumum two numbers

def find_two_maximums(numbers):
    if len(numbers) < 2:
        return "List must contain at least two numbers"
    
    max1, max2 = float('-inf'), float('-inf')
    
    for num in numbers:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
    return max1, max2

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max1, max2 = find_two_maximums(numbers)
print(f"The two maximum numbers are {max1} and {max2}")

#minimum number
def minimum(a,b):
    if a<=b:
        return a
    else:
        return b
a=2
b=4
print(minimum(a,b))

#even odd count
list=[10,21,34,56,67,89,2]
even_count,odd_count=0,0
for num in list:
    if num % 2 == 0:
        even_count+=1
    else:
        odd_count+=1

print("even_number: ",even_count)
print("ood_number: ", odd_count)     

#Find second largest number in list 
list1=[10, 20, 20, 4, 45, 45, 45, 99, 99]
list2=list(set(list1))
list2.sort()

print(list2[-2])
list2.remove(max(list2))
 
# Elements in original list are not changed
# print(list1)
print("Remove maxumum element in list: ",max(list2))

list1=[3646,464,43]
new_list=set(list1)
new_list.remove(max(new_list))
print(max(new_list))





# find out second largest element
list1=[364,23,3,5,5,6]
print("sorted_second_number_in_list: ",sorted(list1)[-2])

def find_second_max(numbers):
    max_num = float('-inf') # Initialize the maximum and second maximum to negative infinity
    second_max = float('-inf')
    for num in numbers:
        if num > max_num: # 
            second_max = max_num  #-1    1  3  1  4 5 2 6 5# Update second_max before updating max_num 0
            max_num = num # 3 4 5 9 
        elif num > second_max and num != max_num: #
            second_max = num
    return second_max  # Return the second maximum valu
list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
result = find_second_max(list1)
print("The second maximum number is:", result)

#method 1
list1=[3,5,8,4]
list1.sort()
print(list1[-2])


#method two
list1=[3,5,8,4]
newlist=set(list1)
newlist.remove(max(newlist))
print(max(newlist))


def secondlargest(numbers):
    max=float('-inf')
    secondmax=float('-inf')
    for num in numbers:
        if num>max:  
            secondmax=max
            max=num
        elif num > secondmax and num != max:
            secondmax=num
    return secondmax
list1=[1,2,4]
resu=secondlargest(list1)
print(resu)



#remove the duplicate from list
 
list = [1,1,3,4,5,5,5,6]

for i in range(len(list)):
    for k in range(len(list)):
        if i == k :#find duplicates first
            continue
        elif list[i] == list[k]:
            del list[k]#deleted duplicate elements
            list.append("0")
          

print(list)
list = [item for item in list if item != '0']
print(list)

list1=[2,3,4,5,2,3,1,5]
new_list=[]
for element in list1:
    if element not in new_list:
       new_list.append(element)
print(new_list)





#String occurances
 
#list comprehension
list2=[2,3,4,5,2,3,1,5]
new2=[]
[new2.append(ele) for ele in list2 if ele not in new2 ]
print(new2)

 #enumerate and list comprehension using index,element/value
list2=[2,3,4,5,2,3,1,5]
new_list=[ele for ind, ele in enumerate(list2) if ele not in list2[:ind]]
print(new_list)


#count duplcates in list
list1 = ["subbu", "rama", "subbu"]
count_dict = {}

for item in list1:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

for key, value in count_dict.items():
    print(f"{key}: {value}")


dict=["subbu","sai","subbu"]
dir={}
for i in dict:
    if i in dir:
        dir[i]+=1
    else:
        dir[i]=1
for key,value in dir.items():
    print(f"{key}:{value}") 
    print(dir)       




#1 convert nested list in single list
def flat(lis):
	flatList = []
	# Iterate with outer list
	for element in lis:
		if type(element) is list:
			# Check if type is list than iterate through the sublist
			for item in element:
				flatList.append(item)
		else:
			flatList.append(element)
	return flatList                   


lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]
print('Flat List', flat(lis))



#2 method
lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]
flatted=[num for sublist in lis for num in sublist]
print(flatted)

'''

        