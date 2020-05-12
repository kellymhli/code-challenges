def get_single_elem(nums) -> int:
    s = set()
    for i in range(len(nums)-1):
        if nums[i] not in s and nums[i] != nums[i+1]:
            return nums[i]
        s.add(nums[i])
    return nums[-1]

print(get_single_elem([1]))  # 1 - single element
print(get_single_elem([1,2,2,3,3,4,4]))  # 1 - first element
print(get_single_elem([1,1,2,3,3,4,4]))  # 2 - inside array
print(get_single_elem([1,1,2,2,3,3,5,5,6,6,8]))  # 8 - last element