def get_running_sm_array(nums):
    """Return the running sum array of a given array."""
    l = len(nums)
    if l <= 1:
        return nums

    res, sm = [0]*l, 0

    for i in range(l):
        sm += nums[i]
        res[i] = sm

    return res

print(get_running_sm_array([1,2,3]))  # [1,3,6]
print(get_running_sm_array([]))  # []
print(get_running_sm_array([5,6,1,2,3,0]))  # [5,11,12,14,17,17]