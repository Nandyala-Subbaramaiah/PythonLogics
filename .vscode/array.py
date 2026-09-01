"""#finding duplicates in array
arr = [1, 2, 3, 4, 2, 7, 8, 8, 3]     
for i in range(0,len(arr)): 
    for j in range(i+1,len(arr)):
        if (arr[i]==arr[j]):
         print(arr[j])
    
#method one
arr1=["subbu","sai","subbu"]
arr2=["subbu","sai","sree"]
seen=set()
for i in range(0,len(arr1)):
      for j in range(0,len(arr2)):
          if (arr1[i]==arr2[j]): 
              seen.add(arr1[i])          
print(seen)

#method two
arr1 = ["subbu", "sai", "subbu"]
arr2 = ["subbu", "sai", "sree"]

seen = set(arr1) & set(arr2)
print(seen)



#printing stars in middle of the strting
arr1 = ["subbu", "sai", "subbu"]
newstr=arr1
newstr='*'.join(newstr)
print(newstr)


arra = [1, 2, 3, 4, 2, 7, 8, 8, 3]
min = arra[0]
for i in arra:
 if i > min:
    print("minimum value is:",min)
    break
else:
    print(i)
    
arrr = [2, 4, 6, 2, 79]
max_val = arrr[0]  # Initialize the maximum value with the first element

for i in arrr:
    if i > max_val:  # If current element is greater than max_val
        max_val = i  # Update max_val

print("Max value:", max_val)



#find two largest numbers in an arraay

array = [2, 3, 41, 2, 4, 6, 7, 77, 77]
max_number = float('-inf')  # Initialize with a very small number
second_max = float('-inf')

for num in array:
    if num > max_number:
        second_max = max_number
        max_number = num
        print(">>>>>>>>>>>>",num)
    elif num > second_max and num != max_number:
        print(">>>><<<<<",num)
        second_max = num
print(">>>>>>>>>>>",second_max)

print("Second Maximum:", second_max)
print("Maximum:", max_number)


#missing number in array
def missing(): 
    array=[1,2,3,4,6,7,8,9]
    sum= 0
    for i in array:
        sum=sum+i 
    sum2=0
    for n in range(10):
        sum2=sum2+n
        missingnumber=sum2-sum
        print(missingnumber)
missing()

array=[1,2,3,2,1]
newarray=array[::-1]
ans=""
for item in array:
    if newarray==array:
        
        print("palindrom",ans)
else:
    print("not a palindrom")
    

#Create a dictionary to store the frequency of each element in the array.
#Iterate through the array and populate the dictionary with the counts.
#Iterate through the array again and find the first element that has a count of one in the dictionary.


def first_non_repeated_element(arr):    
    count_array={}
    for num in arr:
        if num in count_array:
            count_array[num]+=1
        else:
            count_array[num]=1
    for num in arr:
        if count_array[num]==1:
        return num        
    return None    
arr=[3,5,6,7,3,5]
result=first_non_repeated_element(arr)
print(result)

def revesrse(array):

   return array[::-1]

array=[1,5,6,7,3]
result=revesrse(array)
print(result)
           

    
    
    
      
#iterating array elements and store zeros at line end 
#input=[1,2,0,7,3,0,0,10]
#output=[[1, 2, 7, 3, 10, 0, 0, 0]
def countelements_zeros_change_position(arr):
    numberelements=[]
    zeroelements=0
    for num in arr:
        if num !=0:
            numberelements.append(num)
        else:
             zeroelements+=1
    numberelements.extend([0]*zeroelements)
    
    
    return numberelements
    
arr=[1,2,0,7,3,0,0,10]
change_the_position_of_zeros=countelements_zeros_change_position(arr)
print(change_the_position_of_zeros)

def move_zeros(num):
    if len(num)==0: # it will execute if there is no length at that time 
        return []
    # Recursive case
    first=num[0] #Every time picks first element of list with help of the function
    rest=move_zeros(num[1:])
    # this variable works the add append the elements remining list
    if first==0:
        return rest+[0]
    else:
        return [first]+rest
    
list1=[1,2,0,3,4,5,0,1,0,1,2,5]
print(move_zeros(list1)) 


numbers=[]
zero=[]
for num in list1:
    if num==0:
        zero.append(num)
    else:
        numbers.append(num)
res=numbers+zero
print(res)
    
#2nd method  
def countelements_zeros_change_position(arr):
    numberofelements=[num for num in arr if num!=0]
    numberofzeros=[num for num in arr if num==0]
    return numberofelements+numberofzeros

        
arr=[1,2,0,7,3,0,0,10]
change_the_position_of_zeros=countelements_zeros_change_position(arr)
print(change_the_position_of_zeros)



def countarray(array):
    countnumberofelements={}
    for num in array:
        if num in countnumberofelements:
            countnumberofelements[num]+=1
        else:
            countnumberofelements[num]=1
    for num in array:
        if countnumberofelements[num]==1:
           return num
    
    return None
array=[3,4,5,6,7,3,6]
non_repeate=countarray(array)
print(non_repeate)



#date and time ascending order
from datetime import datetime
dates=[datetime(2023,7,15),datetime(2023,12,25),datetime(2023,1,5),datetime(2021,5,20)]

sorted_Items=sorted(dates)
for date in sorted_Items:
    print(date.strftime("%Y-%m-%d"))


def count_occurrences(sorted_array):
    # Dictionary to store the frequency of each element
    frequency_dict = {}

    # Iterate through the sorted array and count occurrences
    for element in sorted_array:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    return frequency_dict

# Example usage
sorted_array = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5]
frequency = count_occurrences(sorted_array)
print(frequency)



def reverse(sorted_array):            
    countoccorances={}
    for num in sorted_array:
         if num in countoccorances:
             countoccorances[num]+=1
         else:
             countoccorances[num]=1
    return countoccorances

sorted_array=[1,1,2,2,3,3,4,5,6,7]
res=reverse(sorted_array)
print(res)

def count_occurrences(sorted_array):
    frequency_dict = {}
    for element in sorted_array:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    return frequency_dict

sorted_array = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5]
frequency = count_occurrences(sorted_array)
print(frequency)


#move all the negitive numbers
def shift_negitive_nums(sorted_array):
    sorted_array.sort()
    for i in sorted_array:
     return sorted_array
sorted_array = [-1, -1, -2, -2, 2, 3, 4, 4, 4, 4, -5]
res=shift_negitive_nums(sorted_array)
print(res) 



#maximum number of array
def maxi_mum_number(lst):
    maximum=list1[0]
    for i in lst:
        if i>maximum:
            maximum=i
    return maximum
    
    
list1=[34,4,6,7,8]
maxi=maxi_mum_number(list1)
print(maxi)    
    
    #list1=[[34,4,-1],[2,4,5,5,-1,-1]]
    #output=[[34, 4, 0], [2, 4, 5, 5, 0, 0]]
    
def maxi_mum_number(lst):
    
   for i in range(len(lst)):
       
       for j in range(len(lst[i])):
           
           if lst[i][j]<0:
               
               lst[i][j]=0
               
   return lst
    
list1=[[34,4,-1],[2,4,5,5,-1,-1]]
maxi=maxi_mum_number(list1)
print(maxi)   

#find the occurances of the array
def occorances(sorted):
    count_occorances={}
    for num in sorted:
        if num in count_occorances:
            count_occorances[num]+=1
        else:
            count_occorances[num]=1
    return count_occorances 
sorted=[1,2,3,5,2,3,6,7,2]
count_occorances=occorances(sorted)
print("count of occorances:", count_occorances )



arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
new_array=sorted(arr)
print(new_array)
# Python Program to sort an array of 0s, 1s and 2s

# Function to sort an array of 0s, 1s and 2s
def sort012(arr):
    c0 = 0
    c1 = 0
    c2 = 0

    # Count 0s, 1s and 2s
    for num in arr:
        if num == 0:
            c0 += 1
        elif num == 1:
            c1 += 1
        else:
            c2 += 1

    idx = 0
    # Place all the 0s
    for i in range(c0):
        arr[idx] = 0
        idx += 1

    # Place all the 1s
    for i in range(c1):
        arr[idx] = 1
        idx += 1

    # Place all the 2s
    for i in range(c2):
        arr[idx] = 2
        idx += 1


# Sample Input
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort012(arr)

for x in arr:
  print(x, end = " ")








list1=[[-1,23,4],[2,4,-4],[6,3,-1]]
for i in range(len(list1)):
    for j in range(len(list1[i])):
         if list1[i][j]<0:
            list1[i][j]=0
print(list1)            


def reverse(sorted_array):            
    countoccorances={}
    for num in sorted_array:
         if num in countoccorances:
             countoccorances[num]+=1
         else:
             countoccorances[num]=1
    return countoccorances

sorted_array=[1,1,2,2,3,3,4,5,6,7]
res=reverse(sorted_array)
print(res)


def countelements_zeros_change_position(arr):
    numberofelements=[num for num in arr if num!=0]
    numberofzeros=[num for num in arr if num==0]
    return numberofelements+numberofzeros
arr=[1,2,0,7,3,0,0,10]
change_the_position_of_zeros=countelements_zeros_change_position(arr)
print(change_the_position_of_zeros)


def m1(arr):
    count_numbers=[]
    count_zeroes=0
    for num in arr:
        if num !=0:
             count_numbers.append(num)
        else:
             count_zeroes+=1
    count_numbers.extend([0]*count_zeroes)
    
    return count_numbers
 
number=[1,2,3,0,5,0]
extend=m1(number)
print(extend)


#number of occorances in sorted_array

def numofoccorances(sorted_array):
 numofoccorancesdict={}
 for num in sorted_array:
      if num in numofoccorancesdict:
         numofoccorancesdict[num]+=1
      else:
        numofoccorancesdict[num]=1
 return numofoccorancesdict
sorted_array=[2,3,4,5,5,6,3,3,5,56]
res=numofoccorances(sorted_array)
print(res)

def longest_subarray_with_sum_k(n, k, a):
    prefix_sum = 0
    max_len = 0
    prefix_map = {}   

    for i in range(n):
        prefix_sum += a[i]

        if prefix_sum == k:
            max_len = i + 1
        
        if (prefix_sum - k) in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - k])

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_len

# Example usage
n = 7
k = 3
a = [1, 2, 3, 1, 1, 1, 1]

# Correct function call
ans = longest_subarray_with_sum_k(n, k, a)
print(ans)  # Output: 3



#Max Contiguous Subarray
nums = [2, -4, 5, -1, 2, -3]
new_dict = {}
length = len(nums)

for i in range(length):
    for j in range(i + 1, length + 1):
        new_dict[tuple(nums[i:j])] = sum(nums[i:j])

        keys = list(new_dict.keys())
        values = list(new_dict.values())

max_index = values.index(max(values))
print(*keys[max_index])

def move_all_zero_elements(arr):
    numberofelements=[]
    numberofzeroelements=0
    for num in arr:
       if num!=0:
         numberofelements.append(num)
       else:
         numberofzeroelements+=1
    numberofelements.extend([0] * numberofzeroelements)
    return numberofelements
arr=[12,3,44,0,2,4,0,3,45,0,1,0]
res=move_all_zero_elements(arr) 
print(res)"""

"""def palindrom(array):
 newarray=array[::-1]
 ans=""
 for i in array:
        if newarray==array:
            print("palindrom",ans)
            break
        else:
            print("not a palindrom")
            break
 return palindrom
array=[1,2,3,2,1]
array=palindrom(array)



def smallest_negitive_number(array):
    smallest_negetive=float('inf')
    for num in array:
        if num < 0 and num < smallest_negetive:
            smallest_negetive=num
        if smallest_negetive==float('inf'):
                return None
        else:
                return smallest_negetive
array=[1,2,-1,-2,-4,2,6,7,-7]
amarray=smallest_negitive_number(array)
print(amarray)


def smallest_positive_number(array):
    smallest_positive=float('inf')
    for num in array:
        if num > 0 and num < smallest_positive:
            smallest_positive=num
    if smallest_positive==float('inf'):
            return None
    else:
            return smallest_positive
array=[1,2,-1,-2,-4,2,6,7,-7]
amarray=smallest_positive_number(array)
print(amarray)

#2 sum problems
class Twosum:
    def __init__(self,list1,target):
      self.list1=list1
      self.target=target
      
    def solution(self):
        length=len(list1)
        
        for i in range(length-1):
            for j in range(i+1,length): 
                if list1[i]+list1[j]==self.target:
                    new_list=i,j
                    return list(new_list)
        return -1  
list1=[1,2,4,5,11]
target=6
obj=Twosum(list1,target)
print("return sum of elements indeces: ",obj.solution())

class Threesum:
    def __init__(self, list1, target):
        self.list1 = list1
        self.target = target

    def solution(self):
        length = len(self.list1)
        
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if self.list1[i] + self.list1[j] + self.list1[k] == self.target:
                        new_list = i, j, k
                        return list(new_list)
        return -1

list1 = [1, 2, 4, 5, 11]
target = 10
obj = Threesum(list1, target)
print("Indices of elements that sum up to target: ", obj.solution())


#repeating number of index dynamically in given array
def find_specific_repeated_index(Array, target, occurrence=2):
    count = 0
    for i in range(len(Array)):
        if Array[i] == target:
            count += 1
            if count == occurrence:
                return i
    return -1  # Return -1 if the specific occurrence is not found

# Example usage:
Array = [1, 2, 3, 4, 5, 3, 6, 7, 8, 5, 3, 3]
target = 3
second_repeated_num_index = find_specific_repeated_index(Array, target)
print(f"Second occurrence of number {target} is at index: {second_repeated_num_index}")"""

"""
def find_specific_repeated_index(Array, target):
    #returns the total number of repeating indeces
    indeces = []
    for i in range(len(Array)):
        if Array[i] == target:
            indeces.append(i)
             
    return indeces
 
    #returns the total number of repeating numbers sum
    total_sum = 0 
    for num in Array: 
        if num == target: 
            total_sum += num
    return total_sum
   
    
# Example usage:
Array = [1, 2, 3, 4, 5, 3, 6, 7, 8, 5, 3, 3]
target = 3
second_repeated_num_index = find_specific_repeated_index(Array, target)
print(f"Second occurrence of number {target} is at index: {second_repeated_num_index}")
 """
"""#find first repeating number in an array
def find_first_repeating_number(Array):
    #find_first_repeating_number
    seen = set()
    for num in Array: 
        if num in seen:
            return num
        seen.add(num)
    return seen  

Array = [1, 2, 3,2, 4, 5, 3, 6, 7, 8, 5, 3]
first_repeating_num = find_first_repeating_number(Array)
print("finding_first_repeating_letter: ",first_repeating_num)

#find non-repeating characters in a string
def find_first_non_repeating_num(array):
    find_first_non_repeating_num_dict={}
    for num in array:
        if num in find_first_non_repeating_num_dict:
            find_first_non_repeating_num_dict[num]+=1
        else:
            find_first_non_repeating_num_dict[num]=1
    for num in array:
        if find_first_non_repeating_num_dict[num]==1:
            return num
    return None

array=[2,3,4,2,3,5,6,7]
fnon_repeating_characters_in_a_string=find_first_non_repeating_num(array)
print("printing find_first_non-repating_num:", fnon_repeating_characters_in_a_string)


class Twosum:
    def __init__(self,list1,target):
        self.list1=list1
        self.target=target
    
    def solution(self):
        lenghth=len(list1)
        
        for i in range(0,lenghth-1):
            for j in range(i+1, lenghth):
                if list1[i]+list1[j]==self.target:
                    
                    new_list=i,j
                    
                    return list(new_list)
        return -1
                
            
list1=[1,2,3,4,5,6]
target=5
obj=Twosum(list1,target)
print(obj.solution())

#fiding duplicates from both sides
def find_duplicates_array(array1,array2):
 sum_duplicates=0
 for i in range(0,len(array1)):
     for j in range(0,len(array2)):
         if array1[i]==array2[j]:
            sum_duplicates+=array1[i]

             
 return sum_duplicates

    
    
    
    
    
array1=[1,2,2,3,4,5,5,6,7,8,9,9]
array2=[2,3,4,2,3,5,6,7,8,7,8,9]
print_duplicates=find_duplicates_array(array1,array2)
print("print sum of duplicates:", print_duplicates)

#finding numbers once and twice
def find_unique_number(arr):
    count_dict = {}
    
    # Count the occurrences of each number
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
            
    unique_number=None
    twice_numbers=[]
    # Find the number that appears once
    for num, count in count_dict.items():
        if count == 1:  
           unique_number=num
        elif count==2:
            twice_numbers.append(num)
        
           
    
    return unique_number, twice_numbers  # Return None if no unique number is found

# Example usage:
arr = [2, 3, 4, 2, 3, 4, 5, 5, 1]
unique_number = find_unique_number(arr)
print(f"The unique number is: {unique_number}")  # Output: The unique number is: 5


#sort 0s,1s and 2s in an array
def sortArray(arr): 
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    for num in arr:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    for i in range(cnt0):
        arr[i] = 0

    for i in range(cnt0, cnt0 + cnt1):
        arr[i] = 1

    for i in range(cnt0 + cnt1, len(arr)):
        arr[i] = 2

arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)
print("After sorting:")
for num in arr:
    print(num, end=" ")
print() 

 
from collections import Counter

def majorityElement(arr):
    # Size of the given array
    n = len(arr)

    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1
 
arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)



def rearrange_alternate(arr):
    positives = [x for x in arr if x >= 0]
    negatives = [x for x in arr if x < 0]
         
    result = []
    i, j = 0, 0
    
    while i < len(positives) and j < len(negatives):
        result.append(positives[i]) 
        result.append(negatives[j])
        i += 1
        j += 1

    # Append remaining elements if any
    result.extend(positives[i:])
    result.extend(negatives[j:])
    
    return result

# Example
arr = [1, -2, 3, -4, 5, -6]
print(rearrange_alternate(arr))  # Output: [1, -2, 3, -4, 5, -6]


#descending and acending order
a = [3, 5, 1, 6, 7, 2, 9]
b = [11, 3, 8]

# Combine the two lists
combined_list = a + b

# Sort the combined list in descending order without using sort()
for i in range(len(combined_list)):
    for j in range(i + 1, len(combined_list)):
        if combined_list[i] < combined_list[j]:
            combined_list[i], combined_list[j] = combined_list[j], combined_list[i]

print(combined_list)

 
#two pointer method 
def two_sum(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        current_sum=nums[left]+nums[right]
        if current_sum==target:
            return left,right
        elif current_sum < target:
            left+=1
        else:
            right-=1
    return None
nums=[2,7,11,15]
target=9
result=two_sum(nums, target)
print(f"printing indeces: ",result)





#Remove duplicates from Sorted Arrayy    Expected Approach - O(n) Time and O(1) Space      
def removeDuplicates(arr):
    n = len(arr)
    # Start from the second element
    idx = 1  
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1

    return idx

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
newSize = removeDuplicates(arr)  

for i in range(newSize): 
    print(arr[i], end=" ")
 

#Works for Unsorted Also - O(n) Time and O(n) Space
def removeDuplicates(arr):
    
    # To track seen elements
    seen = set()
    
    # To maintain the new size of the array
    idx = 0

    for i in range(len(arr)):
        if arr[i] not in seen: 
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx += 1

    # Return the size of the array 
    # with unique elements
    return idx

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    newSize = removeDuplicates(arr)

    for i in range(newSize):
        print(arr[i], end=" ")

def find_missing_numbers(arr, n):
    # Create a set of numbers from 1 to n
    expected_numbers = set(range(1, n + 1))
    # Create a set of numbers in the given array
    actual_numbers = set(arr)
    # Find the difference between the two sets
    missing_numbers = expected_numbers - actual_numbers
    return list(missing_numbers)
                                     
list1 = [1, 2, 5, 6, 7, 8]
n = 10
missing_numbers = find_missing_numbers(list1, n)

print(f'The missing numbers are {missing_numbers}')

#finding longest consequtive elements here 
def linearSearch(a,  num):
    n = len(a)  # size of array
    for i in range(n):
        if a[i] == num:
            return True
    return False


def longestSuccessiveElements(a):
    n = len(a)  # size of array
    longest = 1
    # pick an element and search for its consecutive numbers
    for i in range(n):
        x = a[i]
        cnt = 1
        # search for consecutive numbers using linear search
        while linearSearch(a, x + 1):
            x += 1
            cnt += 1

        longest = max(longest, cnt)
    return longest


a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest co  nsecutive sequence is", ans)


#another method 
def longestSuccessiveElements(a):
    num_set = set(a)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Start of a sequence
            current_num = num
            cnt = 1

            while current_num + 1 in num_set:
                current_num += 1
                cnt += 1

            longest = max(longest, cnt)

    return longest

a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)

def find_countries_for_places(countries_dict, places_list):
    result = {}
    for place in places_list:
        for country, cities in countries_dict.items():
            if place in cities:
                result[place] = country
    return result

# Example dictionary of countries and cities
countries_data = {
    "USA": ["New York", "Los Angeles", "Chicago"],
    "India": ["Mumbai", "Delhi", "Bangalore"],
    "UK": ["London", "Manchester", "Liverpool"],
    "France": ["Paris", "Lyon", "Marseille"]
}

# Example list of places (cities)
places = ["Mumbai", "Chica-go", "Paris", "Liverpool"]

# Get country for each place
result = find_countries_for_places(countries_data, places)

# Print result
print(result)

 
#maxi_mum_product
def maxProduct(arr):
    n=len(arr)
    arr.sort()
    print(arr)
    return max(arr[0]*arr[1]*arr[n-1],arr[n-1]*arr[n-2]*arr[n-3])

    
    
    
arr = [-10, -3, 5, 6, -20]
printing_maxproduct=maxProduct(arr)
print("maxi_mum_product: ", printing_maxproduct)
Time Complexity: O(nlog(n))*
The time complexity measures how the execution time of an algorithm grows with the size of the input data.

In this case:

Sorting the array is the dominant operation in the maxProduct function.

Most efficient sorting algorithms, like Merge Sort or Quick Sort, have a time complexity of O(nlog(n))*.

Here, n is the size of the input array.

log(n) comes from the way sorting algorithms divide the array into smaller parts.

So, O(nlog(n))* means the time taken grows slightly faster than linear but is much better than quadratic (O(n²)).

Space Complexity: O(1)
The space complexity measures how much extra memory the algorithm uses as the input size grows.

O(1) means that the algorithm uses a constant amount of extra memory regardless of the input size.

In this code:

The sorting happens in place, modifying the original array without needing extra storage.

No additional data structures (like lists or dictionaries) are used.
"""
"""def longest_sub_array_with_given_sum_k(arr,k):
    left=0
    current_sum=0
    max_length=0
    for right in range(len(arr)):
        current_sum+=arr[right]
        while current_sum>k:
            current_sum-=arr[left]
        if current_sum==k:
            max_length=max(max_length,right-left+1)
    return max_length
    
arr=[1,2,3,4,5]
k=9
print_longest_sub_array=longest_sub_array_with_given_sum_k(arr,k)
print(print_longest_sub_array)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

odd_num = []
for num in list1:
    if num % 2 == 1:  
        odd_num = [num] + odd_num  


idx = 0
for num in list1:
    if num % 2 == 0:  
        result += [num]
    else:  
        result += [odd_num[idx]]
        idx += 1

print(result)
"""
"""import random

# Example list
my_list = [10, 20, 30, 40, 50]

# Pick one random element
random_element = random.choice(my_list)

# Pick multiple random elements (without replacement)
random_elements = random.sample(my_list, 2)  # Change 3 to the number you want to select
print(f"Random elements: {random_elements}")"""

"""def two_sum(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        current_sum=nums[left]+nums[right]
        if current_sum==target:
            return left,right
        elif current_sum < target:
            left+=1
        else:
            right-=1
    return None
nums=[2,7,11,15]
target=9
result=two_sum(nums, target)
print(f"printing indeces: ",result)"""
       
"""def two_sum1(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        curent_sum=nums[left]+nums[right]
        if curent_sum==target:
            return left,right
        elif curent_sum<target:
            left+=1
        else:
            right-=1
   
    return None
        
nums=[2,7,11,15]
target=9
res=two_sum1(nums,target)
print(res)

def longest_sub_array_with_given_sum_k(arr,k):
    left=0
    current_sum=0
    max_length=0
    for right in range(len(arr)):
        current_sum+=arr[right]
        while current_sum>k:
            current_sum-=arr[left]
            left+=1
        if current_sum==k:
            max_length=max(max_length,right-left+1)
    return max_length
    
arr=[1,2,3,4,5]
k=9
print_longest_sub_array=longest_sub_array_with_given_sum_k(arr,k)
print(print_longest_sub_array)

def moving_zeros_at_end(arr):
    number_elements=[]
    zero_elements=0
    for num in arr:
        if num!=0:
            number_elements.append(num)
        else:
            zero_elements+=1
        
    number_elements.extend([0]*zero_elements)
    return sorted(number_elements)

arr=[1,0,2,0,4,5,7,0,1,0,2,0,5,0]
printing_moving_zeros_at_end=moving_zeros_at_end(arr)
print(printing_moving_zeros_at_end)

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(","}":"{","]":"["}
        for char in s:
            if char in mapping:
                top_element=stack.pop()
                if mapping[char]!=top_element:
                    return False
            else:
                stack.append(char)
        return not stack
        
test_cases=["()","(){}[]{"]
solution=Solution()
#print(solution.isValid(s))
outputs=[]
for test_case in test_cases:
    is_valid=solution.isValid(test_case)
    outputs.append(f"'{test_case}':{is_valid}")
    print("validation res")
    for output in outputs:
            print(output)


def longest_sub_array_with_given_sum_k(arr,k):
    left=0
    current_sum=0
    max_length=0
    for right in range(len(arr)):
        current_sum+=arr[right]
        while current_sum>k:
            current_sum-=arr[left]
            left+=1
        if current_sum==k:
            max_length=max(max_length,right-left+1)
    return max_length
    
arr=[1,2,3,4,5]
k=9
print_longest_sub_array=longest_sub_array_with_given_sum_k(arr,k)
print(print_longest_sub_array)


words = ["cat", "ball", "apple", "carrom", "cotton", "bat", "current", "annotation"]

grouped_words = {}  # Initialize an empty dictionary

for word in words:
    first_char = word[0]  # Get the first character
    if first_char not in grouped_words:
        grouped_words[first_char] = []  # Create a new list if key doesn't exist
    grouped_words[first_char].append(word)  # Append word to the appropriate group

print(grouped_words)

#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_sum=sum(arr[:4])
    max_sum=sum(arr[-4:])
    print(min_sum,max_sum)
    
    return miniMaxSum

    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


def removeDuplicates(arr):
    
    # To track seen elements
    seen = set()
    
    # To maintain the new size of the array
    idx = 0

    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx += 1

    # Return the size of the array 
    # with unique elements
    return idx

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    newSize = removeDuplicates(arr)

    for i in range(newSize):
        print(arr[i], end=" ")

def first_non_repeated_element(arr):
    count_first_repeting={}
    for num in arr:
        if num in count_first_repeting:
            count_first_repeting[num]+=1
        else:
            count_first_repeting[num]=1
    
    for num in arr:
        if count_first_repeting[num]==1:
            return num
    return None

arr=[3,5,6,7,3,5]
result=first_non_repeated_element(arr)
print(result)



def flatten_list(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))   # recursive call
        else:
            result.append(item)
    return result  

print(flatten_list([1, [2, 3], [4, [5, 6]], 7]))
  
a = [3, 5, 1, 6, 7, 2, 9]
b = [11, 3, 8]

# Combine the two lists
combined_list = a + b

# Sort the combined list in descending order without using sort()
for i in range(len(combined_list)):
    for j in range(i + 1, len(combined_list)):
        if combined_list[i] < combined_list[j]:
            combined_list[i], combined_list[j] = combined_list[j], combined_list[i]

print(combined_list)

def two_sum1(nums,target):# following sliding window concept 
    left=0
    right=len(nums)-1
    while left<right:
        curent_sum=nums[left]+nums[right]
        if curent_sum==target:
            return left,right
        elif curent_sum<target:
            left+=1
        else:
            right-=1
   
    return None
        
nums=[2,7,11,15]
target=9
res=two_sum1(nums,target)
print(res)


def find_index(arrr,key):
    for num in range (len(arrr)):
        if arrr[num] == key:
            return num
    return None
arrr=[2,3,4,5,6,7]
key=4
print(find_index(arrr,key))
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

odd_num = []
for num in list1:
    if num % 2 == 1:  
        odd_num = [num]+odd_num

print(odd_num)

idx = 0
for num in list1:
    if num % 2 == 0:  
        result += [num]
    else:  
        result += [odd_num[idx]]
        idx += 1

print(result)
######################## #################### finding index positiion
idx = 0
positions = []

for num in list1:
    if num == 3:
        positions+=[idx]
    idx += 1

print(positions)


def removeDuplicates(arr):
    n = len(arr)
    # Start from the second element
    idx = 1  
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1

    return idx

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
newSize = removeDuplicates(arr)  

for i in range(newSize): 
    print(arr[i], end=" ")


#without using any inbuilt methods moving zeros to end
arr = [2, 0, 4, 0, 10, 0]

index = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[index] = arr[i]
        index += 1

while index < len(arr):
    arr[index] = 0
    index += 1

print(arr)

#find first ans last position for sorted array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=-1
        last=-1
        for i in range(len(nums)):
            if nums[i]==target:
                if first==-1:
                    first=i
                last=i
        return [first, last]

s=Solution()
nums = [5,7,7,8,8,10]
target=8
print(s.searchRange(nums,target))

