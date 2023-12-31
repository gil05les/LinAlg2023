def main():
    matrix = input_square_matrix()

    # makes something special if it is a 1x1 matrix
    if len(matrix) == 1:
        if matrix[0][0] == 0:
            raise ValueError("\nThe matrix you put in isn't invertible, it is singular!")

        else:
            print("\nYour matrix has the size 1x1\n")
            inverse = [[1 / matrix[0][0]]]
            print("The inverse of your matrix is:")
            print(inverse)


    # if it isn't a 1x1 matrix it performs the following path
    else:
        size_matrix = len(matrix)
        check_matrix(matrix, size_matrix)
        identity_matrix = get_identity_matrix(size_matrix)
        augumented_matrix = add_matrices(matrix, identity_matrix)
        new_augumented_matrix = gauss_algorithm(augumented_matrix, size_matrix)
        inverse = get_inverse(new_augumented_matrix, size_matrix)
        print("The inverse of your matrix is:")
        print(inverse)


# gets a square matrix as an input
def input_square_matrix():
    input_matrix = input("\nEnter a square matrix as a nested list (make a list for every row): ")
    matrix = eval(input_matrix)
    return matrix


# calculates the determinant to later see if the matrix is invertible
# for the 2nd part of the function I looked closely into this code: 
# https://stackoverflow.com/questions/3819500/code-to-solve-determinant-using-python-without-using-scipy-linalg-det
def calculate_determinant(matrix, size_matrix):
    if size_matrix == 1:
        return matrix[0][0]
    
    determinant = 0
    for col in range(size_matrix):
        cofactor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        determinant += ((-1) ** col) * matrix[0][col] * calculate_determinant(cofactor, size_matrix - 1)
    return determinant


# checks if the provided matrix is a square matrix, then prints out which size 
# of matrix it is and thenchecks if the determinant, calculated in the function
# before is = 0 if any of these things are wron it rasies an error
def check_matrix(matrix, size_matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("\nThe matrix you put in isn't a square matrix!")
    for row in matrix:
        if len(row) != size_matrix:
            raise ValueError("\nThe matrix you put in hasn't the same number of values in each row!")
    else:
        print(f"\nYour matrix has the size {size_matrix}x{size_matrix}\n")
    determinant = calculate_determinant(matrix, size_matrix)
    if determinant == 0:
        raise ValueError("\nThe matrix you put in isn't invertible, it is singular!")


# makes an identity matrix that has the exact same size as the matrix the user provided
def get_identity_matrix(size_matrix):
    identity_matrix = []
    for i in range(size_matrix):
        row = [] 
        for j in range(size_matrix):
            if i == j: 
                row.append(1)
            else:
                row.append(0)
        identity_matrix.append(row)
    return identity_matrix


# combines the two matrices (the one of the input and the identity matrix)
def add_matrices(matrix, identity_matrix):
    augumented_matrix = [row_matrix + row_identity_matrix for row_matrix, row_identity_matrix in zip(matrix, identity_matrix)]
    return augumented_matrix


# performs the gauss elimination, with the augmented matrix,
# I used the following website for rough inspiration:
# https://stackoverflow.com/questions/64807423/elimination-matrix-gauss-in-python
def gauss_algorithm(augmented_matrix, size_matrix):
    new_augumented_matrix = [row[:] for row in augmented_matrix]
    for i in range(size_matrix):

        # normalize the pivot row
        pivot_element = new_augumented_matrix[i][i]
        if pivot_element != 1:
            new_augumented_matrix[i] = [element / pivot_element for element in new_augumented_matrix[i]]

        # eliminate other rows for the current column
        for j in range(size_matrix):
            if j != i:
                factor = new_augumented_matrix[j][i]
                new_augumented_matrix[j] = [element - factor * new_augumented_matrix[i][index] for index, element in enumerate(new_augumented_matrix[j])]
    return new_augumented_matrix


# the gauss_algorithm provides a new matrix, of which we can erase the 
# left part so we have only the invers left
def get_inverse(new_augumented_matrix, size_matrix):
    inverse = [row[size_matrix:] for row in new_augumented_matrix]
    return inverse


if __name__ == "__main__":
    main()