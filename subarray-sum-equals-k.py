def subarray_sum(nums, k) -> int:
    d, sm, res = {0: 1}, 0, 0
    for n in nums:
        sm += n
        if sm-k in d:
            res += d[sm-k]
        d[sm] = d.get(sm, 0) + 1
    return res

print(subarray_sum([1,1,1], 2))  #2
print(subarray_sum([1,0,0], 1))  #3