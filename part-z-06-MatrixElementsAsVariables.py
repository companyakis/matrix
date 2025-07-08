# matrix elements as variables

# let's create a 4*3 matrix

a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

shape_a_matrix = a_matrix.shape

print(f"Shape of our matrix: {shape_a_matrix}") # Shape of our matrix: (4, 3)

var_a = a_matrix[1, 1] # 5

print(var_a)

var_b = a_matrix[:, 1] # [ 2  5  8 11]

print(var_b)

var_c = a_matrix[1:2, 0:2] # [[4 5]]

print(var_c) 
