def prod_of_arr_except_self(nums):
    res = [1] * len(nums)

    for i in range(1, len(nums)):
        res[i] = nums[i-1] * res[i-1]

    prod, i = 1, len(nums) - 2
    while i >= 0:
        prod *= nums[i+1]
        res[i] *= prod
        i -= 1
    return res

print(prod_of_arr_except_self([1,2,3,4]))