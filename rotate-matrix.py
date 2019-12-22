"""
Rotate an NxN matrix by by 90 degrees.
>>> mat = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
>>> rotate(mat)
[[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
"""

def rotate(mat):

    n = len(mat)-1

    x = 0
    y = 0
    while x < n:
        while y < n//2:
            tl = mat[y][x]
            mat[y][x] = mat[y][n-x]
            mat[y][n-x] = mat[n-y][n-x]
            mat[n-y][n-x] = mat[n-y][x]
            mat[n-y][x] = tl
            y += 1
        x += 1

    print(mat)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("TESTS PASSED")