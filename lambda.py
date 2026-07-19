add_10 = lambda x: x + 10
print(add_10(5))  


numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)   
print(list(even_numbers))  # Output: [2, 4]
