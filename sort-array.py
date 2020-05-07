def sortArray(nums) -> list:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        l, r, m = [], [], []
        for n in nums:
            if n < nums[mid]:
                l += [n]
            elif n > nums[mid]:
                r += [n]
            else:
                m += [n]
        return sortArray(l) + m + sortArray(r)

print(sortArray([5,2,3,1]))
print(sortArray([5,2,1,1,3,0,0]))