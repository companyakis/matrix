# multiplication

# remember the rule: (a * b) & (b * c) => a * c

matrix_1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) # 3 * 4

print(matrix_1)

"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
"""

matrix_2 = np.array([[13, 14], [15, 16], [17, 18], [19, 20]]) # 4 * 2

print(matrix_2)

"""
[[13 14]
 [15 16]
 [17 18]
 [19 20]]

"""

multiplication_matrix = np.dot(matrix_1, matrix_2) # 3 * 2

print(multiplication_matrix)

"""
[[170 180]
 [426 452]
 [682 724]]
"""
