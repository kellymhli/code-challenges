def maxSubArr(nums, k) -> int:
    d = {0: -1}
    sm, mx = 0, 0
    for i, n in enumerate(nums):
        sm += n
        if sm not in d:
            d[sm] = i
        if sm-k in d:
            mx = max(mx, i - d[sm-k])
    return mx

print(maxSubArr([1,-1,5,-2,3], 3))  # 4
print(maxSubArr([-2,-1,2,1], 1))  # 2