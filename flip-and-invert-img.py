def flipAndInvertImg(A) -> list:
    res = [[] for x in range(len(A))]
    row_len = len(A[0])

    for i in range(len(A)):
        for j in reversed(range(row_len)):
            if A[i][j] == 0:
                res[i] += [1]
            else:
                res[i] += [0]
    return res

print(flipAndInvertImg([[1,1,0],[1,0,1],[0,0,0]]))  # [[1, 0, 0], [0, 1, 0], [1, 1, 1]]