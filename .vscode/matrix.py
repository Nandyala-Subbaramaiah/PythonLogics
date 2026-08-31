#2. Matrix Addition
#Adding two matrices element-wise:

"""A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print(result)


#matrix multiplication
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)
print(result)



#cancatenate two matrices
import numpy as np

A1=np.array([[1,2],[3,4]])
B1=np.array([[5,6],[7,7]])
c1=np.concatenate((A1,B1))
print(c1)

# Function to store the transpose of mat in res
def transpose(mat):
  
    # Fill res with transposed values of mat
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

mat = [
    [1, 2, 3],
    [4, 5, 6]
]
    # Function call to calculate the transpose
res = transpose(mat)

    # Print the result matrix
print("Result matrix is:")
for row in res:
    print(" ".join(map(str, row)))


#addition program 
import numpy as np

# Define two matrices
A = np.array([ [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4] ])
B = np.array([ [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4] ])
# Perform matrix addition
result = A + B  # Alternatively, you can use np.add(A, B)

print("\nSum of A and B:")
print(result)


#substarction program
import numpy as np

# Define two matrices
A = np.array([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
])

B = np.array([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
])

# Perform matrix subtraction
result = A - B  # Alternatively, you can use np.subtract(A, B)

print("\nSubtraction of A and B:")
print(result)

import numpy as np

# Define two matrices
A = np.array([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
])

B = np.array([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
])

# Perform element-wise multiplication
result_elementwise = A * B  # Alternatively, np.multiply(A, B)
print(result_elementwise)



import numpy as np

# Define the matrix
v = np.array([[5, 4, 7], 
              [1, 3, 8], 
              [2, 9, 6]])

# Sort the matrix row-wise
sorted_rows = np.sort(v, axis=1)

print("\nRow-wise Sorted Matrix:")
print(sorted_rows)

# Sort the matrix column-wise
sorted_columns = np.sort(v, axis=0)

print("\nColumn-wise Sorted Matrix:")
print(sorted_columns)

# Sort the entire matrix as a flattened array
sorted_flattened = np.sort(v.flatten())

print("\nFully Sorted Matrix:")
print(sorted_flattened.reshape(v.shape))


def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))] 
    # mat[j][i] is used to access the elements of the original matrix in a transposed manner. The outer list comprehension iterates over the columns (i) of the original matrix, while the inner list comprehension iterates over the rows (j). This effectively swaps the rows and columns, resulting in the transposed matrix.


mat=[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

res = transpose(mat)
for row in res:
    print(row)

#rectangle method 2rows*4columns
def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
for row in transpose(mat):
    print(row)


#3×2 matrix
def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]


mat = [
    [10, 20],
    [30, 40],
    [50, 60]
]
for row in transpose(mat):
    print(row)


def transpose(mat):
    result = []

    for i in range(len(mat[0])):
        new_row = []

        for j in range(len(mat)):
            if mat[j][i] >= 0:
                new_row.append(mat[j][i])

        result.append(new_row)

    return result


mat = [
    [-1, 2],
    [3, -4],
    [6, 7]
]

result = transpose(mat)

for row in result:
    print(row)

#diagnol matrix
from ast import main


mat = [
[1, 2, 3], 
[4, 5, 6],
[7, 8, 9]
]
total=0
for i in range(len(mat)):
    # total+=mat[i][i]
    # print(total)
    # total+=mat[i][len(mat)-1-i]
    # print(total)
    total+=mat[i][i]+mat[i][len(mat)-1-i] 
 
    i=0
    main diagnoal mat[0][0] = 1
    secondary diagonal mat[0][3-1-0]
                        = mat[0][2]
                        = 3
                    total+=1+3=4
    i = 1
    main diagnol = mat[1][1] = 5
    Secondary:

                        mat[1][3-1-1]
                        = mat[1][1]
                        total= 5+5=10

    i=2   same loop again here also 
    #The reason we use one loop is that both diagonals have exactly one element in every row
print(total)

#searches in matrix

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == target:
            print("found")
            print(f"Element {target} found at position ({i}, {j})")
            break
    else:
        continue
    break


#count of element's of matrix
mat = [
    [1, 2, 3],
    [2, 5, 2],
    [7, 2, 2]
]

target = 2

count=0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == target:
            count += 1
print(count)

mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
largest=mat[0][0]

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j]>largest:
            largest=mat[i][j]
print(largest)

mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

max_sum=0
max_col=0

for i in range(len(mat)):
    total=0
    for j in range(len(mat[0])):
            total+=mat[i][j]
    if total>max_sum:
        max_sum=total
        max_col=j
print("max_col: ", max_col, "max sum: ", max_sum)
"""