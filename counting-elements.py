def countElems(nums) -> int:
    s, count = set(nums), 0
    for n in nums:
        if n+1 in s:
            count += 1
    return count

print(countElems([1,1,2]))
print(countElems([0,0]))