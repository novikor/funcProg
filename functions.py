import numpy as np


def get_matrix_from_input(rows=None, cols=None):
    if rows and cols:
        print('Please enter a matrix ' + str(rows) + 'x' + str(cols))
    else:
        rows = int(input('Rows count: '))
        cols = int(input('Columns count: '))
    input_string = ''
    try:
        for r in range(rows):
            input_string += input('Row [' + str(r) + '] = ') + ';'
        matrix = np.matrix(input_string.strip(';'))
        if matrix.shape != (rows, cols):
            raise ValueError('Entered rows/cols count do not match with matrix entered')
    except ValueError as e:
        print(e.__str__())
        return get_matrix_from_input(rows, cols)

    return matrix


def add_matrix():
    print('Please enter matrix A:\n')
    a = get_matrix_from_input()
    b = get_matrix_from_input(a.shape[0], a.shape[1])
    print('Result: \n')
    print(np.add(a, b))


def subtract_matrix():
    print('Please enter matrix A:\n')
    a = get_matrix_from_input()
    b = get_matrix_from_input(a.shape[0], a.shape[1])
    print('Result: \n')
    print(np.subtract(a, b))


def get_determinant():
    print('Please enter matrix A:\n')
    print('Determinant: {0:.2f}'.format(np.linalg.det(get_matrix_from_input())))


def transpose():
    print('Please enter matrix A:\n')
    print('Result: \n')
    print(np.matrix.transpose(get_matrix_from_input()))


def multiply_matrix():
    print('Please enter matrix A:\n')
    a = get_matrix_from_input()
    num = int(input('Please enter a multiplier: '))
    print('Result: \n {}'.format(num * a))
