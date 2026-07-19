
"""def square_numbers(numbers):
    for num in numbers:
        yield num ** 2

numbers = [1, 2, 3, 4, 5]
squares = square_numbers(numbers)

print(list(squares))  # Output: [1, 4, 9, 16, 25]
"""
def even_numbers(nums):
    for num in nums:
        if num%2==0:
            yield num
        
    
nums=[1,2,4,5,6,7,8,9]
evens=list(even_numbers(nums))
print(evens)   