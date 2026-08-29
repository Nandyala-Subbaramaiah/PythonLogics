"""#Iterative Binary Search Algorithm: O(log n) Time and O(1) Space
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1
        
    # If we reach here, then the element
    # was not present
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binarySearch(arr, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

#[Naive Approach] - Using Iteration - O(n) Time and O(1) Space
# Function for finding first and last occurrence of x
def find(arr, x):
    n = len(arr)
    
    # Initialize first and last index
    first = -1
    last = -1
    
    for i in range(n):
        
        # If x is different, continue
        if x != arr[i]:
            continue
        
        # If first occurrence found
        if first == -1:
            first = i
        
        # Update last occurrence
        last = i
    res = [first, last]
    return res

if __name__ == "__main__":
    arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    x = 5
    res = find(arr, x)
    print(res[0], res[1])

#[Naive approach] Using linear Search - O(n) Time and O(1) Space
def countOnes(arr):
    count=0
    for num in arr:
        if num == 1:
            count += 1  
        else:
            break
    return count
arr = [1, 1, 0, 0, 0, 0, 0]
print(countOnes(arr))

#[Naive Approach] Using Linear Search - O(n) Time and O(1) Space
def Search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3

    index = Search(arr, key)
    print(index)

# Python program to find minimum element in a 
# sorted rotated array using linear search

def findMin(arr):
    res = arr[0] 

    # Traverse over arr[] to find minimum element
    for i in range(1, len(arr)):
        res = min(res, arr[i]) 
    
    return res

if __name__ == "__main__":
    arr = [5, 6, 1, 2, 3, 4]
    print(findMin(arr))

#method 1
#o(n) Time and o(n) space
def pushZerosToEnd(arr):
    n = len(arr)
    temp = [0] * n

    #to keep track of the index in temp[]
    j=0

    for i in range(n):
        if arr[i]!=0:
            temp[j]=arr[i]
            j+=1
    
    #Fill remaining position in temp[] with zeros
    while j<n:
        temp[j]=0
        j+=1

    #copy all elements from temp[] with zeros
    for i in range(n):
        arr[i]=temp[i]

if __name__=="__main__":
    arr=[1,2,0,4,3,0,5,0]
    pushZerosToEnd(arr)

    for num in arr:
        print(num, end=" ")

#method2
#o(n) Time and o(1) Space
def pushZerosToEnd(arr):

    #pointer to track the position
    #for next non-zero elements
    count=0
    for i in range(len(arr)):

        #If current element is non-zero
        if arr[i]!=0:

            #Swap the current element with
            #the 0 at index "count"
            arr[i], arr[count] = arr[count], arr[i]

            #Move "count" pointer to the nect position
            count+=1
            

if __name__=="__main__":
    arr=[1,2,0,4,3,0,5,0]
    pushZerosToEnd(arr)

    for num in arr:
        print(num, end=" ")

#[Approach 1] Usingg visited Array - o(n) Time and o(n) space
def findTwoElement(arr):
    n=len(arr)
    freq=[0]*(n+1)

    repeating=-1
    missing=-1

    for num in arr:
        freq[num]+=1
    
    for i in range(1, n+1):
        if freq[i] == 0:
            missing=i
        elif freq[i] == 2:
            repeating=i
    return [missing, repeating]


if __name__ == "__main__":
    arr=[3,1,3]
    ans=findTwoElement(arr)
    print(ans[0],ans[1])


#hashing  -o(n) Time and o(n) Space
def missingNum(arr):
    n=len(arr)+1

    #Create hash array of size n+1
    hash=[0]*(n+1)

    #store frequencies of elements
    for i in range(n - 1):
        hash[arr[i]]+=1
    
    #find the missing number
    for i in range(1, n+1):
        if hash[i] == 0:
            return i
    return -1

if __name__ == "__main__":
    arr=[8,2,4,5,3,7,1]
    res=missingNum(arr)
    print(">>>>> res ",res)


#[Expected Approach 1] Using Sum of n terms Formula - o(n) Time And O(1) Space
def missingNum(arr):
    n=len(arr)+1


    #Calculate the sum of array elements
    totalSum=sum(arr)

    #calculate the expected sum of array elements
    expSum=n*(n+1)//2

    return expSum - totalSum   

if __name__ == "__main__":
    arr=[8,2,4,5,3,7,1]
    res=missingNum(arr)

#prefix sum implementation #Time complixity o(n) and space complixity (n)
def prefixSum(arr):
    n=len(arr)

    #to store the prefixsum
    prefixSum=[0]*n

    #initialize the first element
    prefixSum[0]=arr[0]

    #adding present element with previouse element
    for i in range(1,n):
        prefixSum[i]=prefixSum[i-1]+arr[i]
    return prefixSum

if __name__=="__main__":
    arr=[1,2,3,4,5]
    preSum=prefixSum(arr)
    for i in preSum:
        print(i, end=" ")

#time complixity o(n) and space complixity o(n)
def brackets_balanced(s):
    stack=[]
    bracket_map={')':'(', '}':'{', ']':'['}
    opening_brckets={'(', '{', '['}
    
    for char in s:
        if char in opening_brckets: 
            stack.append(char)
        elif char in bracket_map: #it' s a closing bracket
            if not stack or stack.pop() != bracket_map[char]:
                return False #mismatched or unclosed bracket
        # ignore other characters
    return not stack #True if stack is empty , False otherwise


print(brackets_balanced("()")) 
print(brackets_balanced("(){}[]"))
print(brackets_balanced("(]"))
print(brackets_balanced("([)]"))
print(brackets_balanced("{[]}"))
print(brackets_balanced("({[)]})"))
print(brackets_balanced("]"))
print(brackets_balanced(""))

def reverse_vowels(s):
    vowels=set("aeiouAEIOU")
    s_list=list(s)          #convert to list so we can mutate characters
    left, right=0, len(s_list)-1

    while left<right:
        #move left pointer untill we find a vowel (or left>=right)
        while left < right and s_list[left] not in vowels:
            left+=1
        #move right pointer until we find a vowel(or left >= right)
        while left < right and s_list[right] not in vowels:
            right-=1
        if left < right:
            #swp the vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left+=1
            right-=1
            
    return "".join(s_list)

if __name__=="__main__":
    s="oranges"
    print(reverse_vowels(s))"""

def missingNum(arr):
    n=len(arr)+1


    #Calculate the sum of array elements
    totalSum=sum(arr)

    #calculate the expected sum of array elements
    expSum=n*(n+1)//2

    return expSum - totalSum   

if __name__ == "__main__":
    arr=[8,2,4,5,3,7,1]
    res=missingNum(arr)
    print(res)
