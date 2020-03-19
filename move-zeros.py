def moveZeros(nums):
    to_check = len(nums)
    i = 0
    while i < to_check:
        if nums[i] == 0:
            nums.append(nums.pop(i))
            to_check -= 1
        else:
            i += 1
    return nums

print(moveZeros([1,2,0,1,2,3,0,3,0]))
print(moveZeros([0,0,1,0,1,0]))
print(moveZeros([]))