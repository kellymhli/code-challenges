def single_number(nums) -> list:
    """Return a list of the two numbers that occur only once in the array."""
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1

    return [k for k, v in d.items() if v == 1]

print(single_number([1,2,1,3,2,5]))  # [3,5]
print(single_number([1,2,3,8,2,3,4,4,5,6,5,6]))  # [1,8]
