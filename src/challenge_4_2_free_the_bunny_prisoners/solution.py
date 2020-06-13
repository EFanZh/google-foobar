def solution_helper(num_buns, num_required, matrix, row_index, column_index):
    """
    +------------------------------+----------------------------------+
    | ............................ |                                  |
    +------------------------------+----------------------------------+
    | (num_buns - 1, num_required) | (num_buns - 1, num_required - 1) |
    +------------------------------+----------------------------------+
    """

    if num_required == 1:
        for row in matrix[row_index:]:
            row.append(column_index)

        return column_index + 1
    elif num_buns == num_required:
        for i, row in enumerate(matrix[row_index:], column_index):
            row.append(i)

        return column_index + num_buns
    else:
        first_row = matrix[row_index]
        middle = solution_helper(num_buns - 1, num_required, matrix, row_index + 1, column_index)

        for i in range(column_index, middle):
            first_row.append(i)

        return solution_helper(num_buns - 1, num_required - 1, matrix, row_index + 1, middle)


def solution(num_buns, num_required):
    result = [[] for _ in range(num_buns)]

    solution_helper(num_buns, num_required, result, 0, 0)

    return result
