def majorityElement(nums) -> int:
    """
    Given a list of nums, return the majority element.
    A majority element appears more than n/2 times where n is the size of the list.
    """
    d = {}
    half_n = len(nums)//2

    for n in nums:
        d[n] = d.get(n, 0) + 1
        if d[n] > half_n:
            return n
    return -1

print(majorityElement([3,2,3]))  # 3
print(majorityElement([2,2,1,1,2,2]))  # 2