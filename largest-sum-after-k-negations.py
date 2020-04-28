def largest_sum(nums, k) -> int:
    nums.sort()
    i = 0

    while k > 0:
        if nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1
        elif nums[0] == 0:
            k = 0
        else:
            if k % 2 == 1:
                nums.sort()
                nums[i] = -nums[i]
            break
    return sum(nums)

print(largest_sum([4,2,3], 1))  # 5
print(largest_sum([3,-1,0,2], 3))  # 6