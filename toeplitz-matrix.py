def isToeplitz(matrix):
    d = {}
    for i, lst in enumerate(matrix):
        for j, val in enumerate(lst):
            if i-j not in d:
                d[i-j] = val
            elif d[i-j] != val:
                return False
    return True

print(isToeplitz([[1,2], [3,1]]))
print(isToeplitz([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(isToeplitz([[1,2,3], [4,1,2], [7,8,1]]))