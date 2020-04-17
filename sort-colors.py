def sort_colors(nums):
    """Sort array containing 0, 1, and 2 in place."""
    i, l = 0, len(nums)-1

    while i <= l:
        if nums[i] == 0:
            nums.insert(0, nums.pop(i))
            i += 1
        elif nums[i] == 2:
            nums.append(nums.pop(i))
            l -= 1
        else:
            i += 1
    return nums

print(sort_colors([2,0,2,1,1,0])) # [0,0,1,1,2,2]
print(sort_colors([1,2,1,0,0,1,1,2,1]))  # [0,0,1,1,1,1,1,2,2]
print(sort_colors([]))  # []