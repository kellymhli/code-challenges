def mutiply_matrix( A, B):
    m, n = len(A), len(B[0])
    res = [[0]*n for i in range(m)]

    for i in range(m):
        for j in range(len(A[0])):
            for k in range(n):
                res[i][k] = A[i][j]*B[j][k]
    return res

res = mutiply_matrix([[1, 2, 4]], [[3], [4], [5]])
print(res)