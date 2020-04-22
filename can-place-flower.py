def can_place_flower(bed, n):
    res = 0
    A = [0] + bed + [0]

    for i in range(1, len(A)-1):
        if A[i-1] == A[i] == A[i+1] == 0:
            A[i] = 1
            res += 1

    return res >= n

print(can_place_flower([1,0,1,0,1,0,1], 0))  # T
print(can_place_flower([1,0,0,0,1], 1))  #T
print(can_place_flower([1,0,0,0,1], 2))  #F