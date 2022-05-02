# Python 3 Representation of matrix A

matrix_A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# Accessing Matrix A
print('Row 1: %s' % matrix_A[0]) # Recall: Indexing starts at zero in Python
print('Value at Row 2 Column 2: %s' % matrix_A[1][1])

# Old Method
squares = []
for i in range(10):
    squares.append(i ** 2)

print('Our result: %s' % squares)

# List Comprehension

squares = [i**2 for i in range(10)]

print('Our new result: %s' % squares)

# Solution
a = [1,2,3]
b = [3,1,4]

result = [[x, y] for x in a for y in b if x != y]
print(result)

#example 3
vec = [[1,2,3], [4,5,6], [7,8,9]]

result = [value for row in vec for value in row]

print('Vec as a single list of values: %s' % result)

