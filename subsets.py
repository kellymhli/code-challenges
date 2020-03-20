def get_subsets(nums):
    res = [[]]
    for n in nums:
        res += [lst + [n] for lst in res]
    return res

print(get_subsets([]))
print(get_subsets([1,1]))
print(get_subsets([1,2,3]))