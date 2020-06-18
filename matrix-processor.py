# Stage 5/6
# Determined!
# Stage 6/6
# Inverse matrix


import decimal

decimal.getcontext().rounding = decimal.ROUND_DOWN

def create_matrix(number=""):
    m, n = [int(x) for x in input(f"Enter size of {number}matrix: ").split()]
    print(f"Enter {number}matrix: ")
    return [[float(x) for x in input().split()] for row_matrix in range(int(m))]


def add_matrices():
    matrix_1 = create_matrix("first ")
    matrix_2 = create_matrix("second ")

    m_1, m_2 = len(matrix_1), len(matrix_2)
    n_1, n_2 = len(matrix_1[0]), len(matrix_2[0])

    if m_1 != m_2 or n_1 != n_2:
        print("The operation cannot be performed.")
        exit()

    m = m_1
    n = n_1

    matrix_3 = [[(matrix_1[x][y] + matrix_2[x][y]) for y in range(n)] for x in range(m)]

    for row in matrix_3:
        for column in row:
            print(column, end=" ")
        print()

    print()
    main()


def multiply_by_constant():
    matrix = create_matrix()
    row, column = len(matrix), len(matrix[0])

    print("Enter constant: ")
    n = float(input())
    matrix_constant = [[n * matrix[x][y] for y in range(column)] for x in range(row)]

    for row in matrix_constant:
        for column in row:
            print(column, end=" ")
        print()

    print()
    main()


def multiply_matrices():
    matrix_1 = create_matrix("first ")
    matrix_2 = create_matrix("second ")

    m_1, m_2 = len(matrix_1), len(matrix_2)
    n_1, n_2 = len(matrix_1[0]), len(matrix_2[0])

    if n_1 != m_2:
        print("The operation cannot be performed.")
        exit()

    m = m_1
    p = n_1
    n = n_2

    matrix_3 = [[sum([(matrix_1[x][z] * matrix_2[z][y]) for z in range(p)]) for y in range(n)] for x in range(m)]

    for row in matrix_3:
        for column in row:
            print(column, end=" ")
        print()

    print()
    main()


def transpose_diagonal(matrix, m, n):

    matrix_t_diagonal = [[matrix[x][y] for x in range(m)] for y in range(n)]

    for row in matrix_t_diagonal:
        for column in row:
            print(column, end=" ")
        print()

    print()
    main()


def transpose_side(matrix, m, n):

    matrix_t_side = [[matrix[m - 1 - x][n - 1 - y] for x in range(m)] for y in range(n)]

    for row in matrix_t_side:
        for column in row:
            print(column, end=" ")
        print()

    print()
    main()


def transpose_vertical(matrix, m, n):

    matrix_t_vertical = [[matrix[x][n - 1 - y] for y in range(n)] for x in range(m)]

    for row in matrix_t_vertical:
        for column in row:
            print(column, end=" ")
        print()

    print()
    main()


def transpose_horizontal(matrix, m, n):

    matrix_t_horizontal = [[matrix[m - 1 - x][y] for y in range(n)] for x in range(m)]

    for row in matrix_t_horizontal:
        for column in row:
            print(column, end=" ")
        print()

    print()
    main()


def matrix_minor(matrix, i, j):
    m, n = len(matrix), len(matrix[0])
    if m > 1 and n > 1:
        minor = [[matrix[x][y] for y in range(n) if y != j] for x in range(m) if x != i]
        return minor

def matrix_determinant(matrix, n):
    global det

    if len(matrix[0]) != n:
        print("The operation cannot be performed.")
        exit()

    if n == 1:
        return matrix[0][0]

    # base case, must return a value:
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    if n > 2:
        det = 0
        for y in range(len(matrix)):
            m = matrix_minor(matrix, 0, y)
            det = det + ((-1) ** (y + 2)) * matrix[0][y] * matrix_determinant(m, n - 1)
        return det


def matrix_inverse():
    mtx = create_matrix()
    a, b = len(mtx), len(mtx[0])

    if a != b:
        print("This matrix doesn't have an inverse.")
    if a == b:
        d = matrix_determinant(mtx, a)
        print(f"matrix deterrminant is {d}")
        if d == 0:
            print("This matrix doesn't have an inverse.")
        if d != 0:
            minor = [[(matrix_determinant(matrix_minor(mtx, x, y), a - 1) * (-1) ** (x + y + 2)) for y in range(a)] for x in range(a)]
            print(f"minor is {minor}")
            transpose = [[minor[x][y] for x in range(a)] for y in range(a)]
            print(f"transpose is {transpose}")

            inverse = [[round(decimal.Decimal(1 / d * transpose[x][y]), 2) for y in range(a)] for x in range(a)]
            print(f"inverse is {inverse}")

            print("The result is: ")
            for row in inverse:
                for column in row:
                    if column == - 0.0:
                        column = 0.0
                    print(column, end=" ")
                print()

        print()
        main()

def main():
    print("1. Add matrices\n2. Multiply matrix by a constant\
    \n3. Multiply matrices\n4. Transpose\n5. Calculate a determinant\
    \n6. Inverse matrix\n0. Exit")
    choice = input("Your choice: ")
    if choice == "1":
        add_matrices()
    elif choice == "2":
        multiply_by_constant()
    elif choice == "3":
        multiply_matrices()
    elif choice == "4":
        print("1. Main diagonal\n2. Side diagonal\
        \n3. Vertical line\n4. Horizontal line")
        transpose_choice = input("Your choice: ")

        mtx = create_matrix()
        a, b = len(mtx), len(mtx[0])

        if transpose_choice == "1":
            transpose_diagonal(mtx, a, b)
        elif transpose_choice == "2":
            transpose_side(mtx, a, b)
        elif transpose_choice == "3":
            transpose_vertical(mtx, a, b)
        elif transpose_choice == "4":
            transpose_horizontal(mtx, a, b)
    elif choice == "5":
        mtx = create_matrix()
        print("The result is: ")
        print(matrix_determinant(mtx, len(mtx)))
        print()
        main()
    elif choice == "6":
        matrix_inverse()

    if choice == "0":
        exit()

main()

