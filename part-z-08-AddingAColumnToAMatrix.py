# adding a column to a matrix

a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(a_matrix)

"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

"""

a_matrix_new = np.hstack((a_matrix, np.array([[50], [100], [150], [200]])))

print(a_matrix_new)

"""
[[  1   2   3  50]
 [  4   5   6 100]
 [  7   8   9 150]
 [ 10  11  12 200]]
"""
