# delete a row or a column
# delete a row if axis = 0
# delete a column if axis = 1

matrix_A = np.array([[3, 2.5, 0, 1], [2.7, 4, 1, 21], [2.6, 0, 11, 3]])

print(matrix_A)

"""
[[ 3.   2.5  0.   1. ]
 [ 2.7  4.   1.  21. ]
 [ 2.6  0.  11.   3. ]]

"""
# let's delete row 2
new_matrix_B = np.delete(matrix_A, 1, 0)

print(new_matrix_B)

"""
[[ 3.   2.5  0.   1. ]
 [ 2.6  0.  11.   3. ]]
"""

# let's delete column 3
new_matrix_C = np.delete(matrix_A, 2, 1)

print(new_matrix_C)

"""
[[ 3.   2.5  1. ]
 [ 2.7  4.  21. ]
 [ 2.6  0.   3. ]]
"""
