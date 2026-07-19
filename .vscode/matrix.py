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
"""