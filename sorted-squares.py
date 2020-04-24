def sorted_squares(nums):
    return sorted(n*n for n in nums)

print(sorted_squares([-1,1,2,3]))  #[1,1,4,9]