"""
Rotate an NxN matrix by by 90 degrees.
>>> mat = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
>>> rotate(mat)
[[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
"""

def rotate(mat):

    n = len(mat)-1

    i = 0
    while i < n:
        curr = mat[i][i]
        nxt = mat[i][n-i]
        mat[i][n-i] = curr
        curr = nxt

        nxt = mat[n-i][n-i]
        mat[n-i][n-i] = curr
        curr = nxt

        nxt = mat[n-i][i]
        mat[n-i][i] = curr
        mat[i][i] = nxt
        i += 1

    print(mat)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("TESTS PASSED")