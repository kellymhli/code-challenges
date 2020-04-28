def largest_sum(nums, k) -> int:
    nums.sort()
    i = 0

    while k > 0:
        if nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1
        elif nums[i] == 0:
            k = 0
        else:
            if k % 2 == 1:
                nums.sort()
                nums[0] = -nums[0]
            break
    return sum(nums)

print(largest_sum([4,2,3], 1))  # 5
print(largest_sum([3,-1,0,2], 3))  # 6
print(largest_sum([-4,-6,9,-2,2], 4))  # 19