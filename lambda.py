add_10 = lambda x: x + 10
print(add_10(5))  


numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)   
print(list(even_numbers))  # Output: [2, 4]


salaries=[33000.0, 49500.0, 55000.0, 66000.0, 88000.0]
high_salaries = list(
    filter(lambda salary: salary > 50000, salaries)
)

print(high_salaries)