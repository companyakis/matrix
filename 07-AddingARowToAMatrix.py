# adding a row to a matrix

a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(a_matrix)

"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

"""

a_matrix_new = np.vstack((a_matrix, np.array([-1, -2, -3])))

print(a_matrix_new)

"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]
 [-1 -2 -3]]

"""
