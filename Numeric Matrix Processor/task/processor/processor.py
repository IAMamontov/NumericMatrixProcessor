

main_menu = """
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
"""
transpose_menu = """1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line"""


def fill_matrix(n, m, matrix):
    for i in range(n):
        matrix.append(list(map(float, input().split(maxsplit=m))))


def map_matrix(matrix_in, operation):
    matrix_out = []
    for i in range(len(matrix_in)):
        matrix_out.append([])
        for j in range(len(matrix_in[i])):
            matrix_out[i].append(operation(matrix_in[i][j]))
    return matrix_out


def ridiculous_convert(x):
    i, f = str(float(x)).split(".")
    if f == "0":
        return int(i)
    else:
        s = i + "." + f[:2]
        return float(s)


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if isinstance(matrix[i][j], int):
                print("{: 4}".format(matrix[i][j]), end=" ")
            else:
                print("{: }".format(matrix[i][j]), end=" ")
        print()


def add_matrix(matrix_in_1, matrix_in_2):
    matrix_out = []
    if len(matrix_in_1) != len(matrix_in_2) or len(matrix_in_1[0]) != len(matrix_in_2[0]):
        return "The operation cannot be performed."
    for i in range(len(matrix_in_1)):
        matrix_out.append([])
        for j in range(len(matrix_in_1[i])):
            matrix_out[i].append(matrix_in_1[i][j] + matrix_in_2[i][j])
    return matrix_out


def mul_matrix_c(matrix_in, c):
    matrix_out = []
    for i in range(len(matrix_in)):
        matrix_out.append([])
        for j in range(len(matrix_in[i])):
            matrix_out[i].append(matrix_in[i][j] * c)
    return matrix_out


def dot_product(list1, list2):
    if len(list1) != len(list2):
        return None
    else:
        s = 0
        for i in range(len(list1)):
            s = s + list1[i] * list2[i]
        return s


def mul_two_matrix(matrix_in_1, matrix_in_2):
    matrix_out = []
    if len(matrix_in_1[0]) != len(matrix_in_2):
        return "The operation cannot be performed."
    else:
        for i in range(len(matrix_in_1)):
            matrix_out.append([])
            for j in range(len(matrix_in_2[i])):
                m2_col = [sub[j] for sub in matrix_in_2]
                matrix_out[i].append(dot_product(matrix_in_1[i], m2_col))
        return matrix_out


def transform_main_diagonal(matrix_in):
    matrix_out = []
    for i in range(len(matrix_in)):
        matrix_out.append([])
        for j in range(len(matrix_in[i])):
            matrix_out[i].append(matrix_in[j][i])
    return matrix_out


def transform_side_diagonal(matrix_in):
    matrix_out = []
    for i in range(len(matrix_in)):
        matrix_out.append([])
        for j in range(len(matrix_in[i])):
            matrix_out[i].append(matrix_in[-1-j][-1-i])
    return matrix_out


def transform_vertical_line(matrix_in):
    matrix_out = []
    for i in range(len(matrix_in)):
        matrix_out.append([])
        for j in range(len(matrix_in[i])):
            matrix_out[i].append(matrix_in[i][-1-j])
    return matrix_out


def transform_horizontal_line(matrix_in):
    matrix_out = []
    for i in range(len(matrix_in)):
        matrix_out.append([])
        for j in range(len(matrix_in[i])):
            matrix_out[i].append(matrix_in[-1-i][j])
    return matrix_out


def get_matrix_minus_i_j(matrix_in, i_minus, j_minus):
    matrix_out = []
    for i in range(len(matrix_in)):
        if i == i_minus:
            continue
        else:
            matrix_out.append([])
            for j in range(len(matrix_in[i])):
                if j == j_minus:
                    continue
                else:
                    if i > i_minus:
                        ii = i - 1
                    else:
                        ii = i
                    matrix_out[ii].append(matrix_in[i][j])
    return matrix_out


def get_determinant(matrix_in):
    d = 0
    if len(matrix_in) == 1:
        return matrix_in[0][0]
    elif len(matrix_in) == 2:
        return matrix_in[0][0] * matrix_in[1][1] - matrix_in[1][0] * matrix_in[0][1]
    else:
        for j in range(len(matrix_in[0])):
            d = d + matrix_in[0][j] * pow(- 1, j) * get_determinant(get_matrix_minus_i_j(matrix_in, 0, j))
        return d


def get_cofactor_matrix(matrix_in):
    matrix_out = []
    for i in range(len(matrix_in)):
        matrix_out.append([])
        for j in range(len(matrix_in[i])):
            matrix_out[i].append(pow(- 1, i + j) * get_determinant(get_matrix_minus_i_j(matrix_in, i, j)))
    return matrix_out


def get_inverse_matrix(matrix_in):
    c = get_cofactor_matrix(matrix_in)
    ct = transform_main_diagonal(c)
    d = get_determinant(matrix_in)
    if d == 0:
        return "This matrix doesn't have an inverse."
    else:
        multiplier = 1 / d
        matrix_out = mul_matrix_c(ct, multiplier)
        return map_matrix(matrix_out, ridiculous_convert)


def two_operand_operation(operation):
    matrix_1 = []
    matrix_2 = []
    n1, m1 = map(int, input("Enter size of first matrix: ").split())
    print("Enter first matrix:")
    fill_matrix(n1, m1, matrix_1)
    n2, m2 = map(int, input("Enter size of second matrix: ").split())
    print("Enter second matrix:")
    fill_matrix(n2, m2, matrix_2)
    res = operation(matrix_1, matrix_2)
    if isinstance(res, list):
        print("The result is:")
        print_matrix(res)
    elif isinstance(res, str):
        print(res)


def one_operand_operation_with_constant(operation):
    matrix_1 = []
    n1, m1 = map(int, input("Enter size of matrix: ").split())
    print("Enter matrix:")
    fill_matrix(n1, m1, matrix_1)
    c1 = int(input("Enter constant: "))
    res = operation(matrix_1, c1)
    print("The result is:")
    print_matrix(res)


def one_operand_operation(operation):
    matrix_1 = []
    n1, m1 = map(int, input("Enter size of matrix: ").split())
    print("Enter matrix:")
    fill_matrix(n1, m1, matrix_1)
    res = operation(matrix_1)
    if isinstance(res, list):
        print("The result is:")
        print_matrix(res)
    elif isinstance(res, (int, str, float)):
        print(res)


def one_operand_operation_with_menu_choice(menu):
    print(menu)
    choice = int(input("Your choice: "))
    if choice == 1:
        one_operand_operation(transform_main_diagonal)
        return
    elif choice == 2:
        one_operand_operation(transform_side_diagonal)
        return
    elif choice == 3:
        one_operand_operation(transform_vertical_line)
        return
    elif choice == 4:
        one_operand_operation(transform_horizontal_line)
        return


def main_menu_loop():
    while True:
        print(main_menu)
        choice = int(input("Your choice: "))
        if choice == 1:
            two_operand_operation(add_matrix)
        elif choice == 2:
            one_operand_operation_with_constant(mul_matrix_c)
            continue
        elif choice == 3:
            two_operand_operation(mul_two_matrix)
            continue
        elif choice == 4:
            one_operand_operation_with_menu_choice(transpose_menu)
            continue
        elif choice == 5:
            one_operand_operation(get_determinant)
            continue
        elif choice == 6:
            one_operand_operation(get_inverse_matrix)
            continue
        elif choice == 0:
            break


main_menu_loop()
