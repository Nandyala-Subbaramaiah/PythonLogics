"""n=5
for row in range(1,n+1):
    print(" "*(n-row) + "*"*((2*row)-1))

#center pyramid
n=5
for row in range(1,n+1):
    print(" "*(n-row)+"* "*row)
    
"""
#simple pyramid
#Half Pyramid of Stars
"""n=5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
#normal pyramid  
rows=5
for i in range(1, rows+1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
  
#inverted pyramid    
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


rows = 5
for i in range(1, rows + 1):
    if i % 2 != 0:  # Odd rows: print numbers
        for j in range(1, i + 1):
            print(j, end=" ")
    else:  # Even rows: print stars
        for j in range(1, i + 1):
            print("*", end=" ")
    print() 
    
"""
rows = 5

for i in range(1, rows + 1):
    if i % 2 == 1:  # Check if the row number is odd
        for j in range(1, i + 1):
            print('*', end=" ")
    else:  # For even rows, print numbers in reverse order
        for j in range(i, 0, -1):
            print(j, end=" ")
    print()

