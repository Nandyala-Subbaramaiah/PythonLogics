"""def fibonacci_loop(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = 10  # Number of Fibonacci numbers to generate
print(fibonacci_loop(n))

def fibonacci(n):
    # Base cases: fib(0) is 0 and fib(1) is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of the previous two Fibonacci numbers
        return fibonacci(n-1) + fibonacci(n-2)

n = 10  # Example
print([fibonacci(i) for i in range(n)])  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def is_prime_numbers(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%2==0:
            return False
        
    return True
def prime_numbers(n):
    return [num for num in range(2, n+1) if is_prime_numbers(num)]
print(prime_numbers(20))
"""

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))


