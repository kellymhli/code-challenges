"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""

def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    # Empty sets for x and y indecies
    x_index = set()
    y_index = set()

    # ID the index of each 0 in the matrix and add to x and y sets
    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            if col == 0:
                x_index.add(x)
                y_index.add(y)

    # Replace rows that contains 0 with zeros
    for x in x_index:
        for y in range(len(matrix[x])):
            matrix[x][y] = 0

    # Replace columns that contains 0 with zeros
    for y in y_index:
        for x in range(len(matrix)):
            matrix[x][y] = 0

    return matrix


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
