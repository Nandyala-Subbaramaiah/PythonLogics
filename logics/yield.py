
"""def square_numbers(numbers):
    for num in numbers:
        yield num ** 2

numbers = [1, 2, 3, 4, 5]
squares = square_numbers(numbers)

print(list(squares))  # Output: [1, 4, 9, 16, 25]

#generators program function with yield keywors 
def even_numbers(nums):
    for num in nums:
        if num%2==0:
            yield num
        
    
nums=[1,2,4,5,6,7,8,9]
evens=list(even_numbers(nums))
print(evens)   
"""



def generate_numbers():
    for i in range(1, 6):
       yield i

# Create a generator object
gen = generate_numbers()

# Iterate through the generator and print each value
for number in gen:
    print(number)
"""def count_up_to(n):
    i=1
    while i<=n:
        yield i
        i+=1
        
for num in count_up_to(10):
    print(num)"""

