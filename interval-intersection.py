def interval_intersection(A, B) -> list:
    res, i, j = [], 0, 0
    while i < len(A) and j < len(B):
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        if lo <= hi:
            res.append([lo, hi])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return res

print(interval_intersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))  # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]