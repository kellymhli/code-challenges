def minSubseq(nums) -> list:
    nums.sort()
    l, r, res = sum(nums), 0, []
    for i in range(1, len(nums)+1):
        if l >= r:
            l -= nums[-i]
            r += nums[-i]
            res += [nums[-i]]
        else:
            break
    return res

print(minSubseq([4,3,10,9,8]))
print(minSubseq([4,4,7,6,7]))
print(minSubseq([6]))