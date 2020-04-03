def dominant_index(nums):
    """
    Return the index of the dominant number
    if it is at least twice as large as the next largest number.
    """
    print(nums)
    d = {}
    for i, n in enumerate(nums):
        if n not in d:
            d[n] = i

    if len(d) <= 1:
        return 0

    nums.sort()
    if nums[-1] >= nums[-2] * 2:
        return d[nums[-1]]

    return -1

print("Print index of the dominant num if it's at least twice as large as the next largest num. \n")
print(dominant_index([0,0,3,2]))
print(dominant_index([3,6,1,0]))
print(dominant_index([0,0,0,1]))
print(dominant_index([1]))
print(dominant_index([8,8]))