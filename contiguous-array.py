def find_max_len(nums):
    count, mx, d = 0, 0, {0: -1}
    for i, n in enumerate(nums):
        if n == 0:
            count -= 1
        else:
            count += 1

        if count in d:
            mx = max(mx, i - d[count])
        else:
            d[count] = i
    return mx

print(find_max_len([0,1]))  # 2
print(find_max_len([1,1,1,0,0,1,0,1,0,0,1,0]))  # 12
print(find_max_len([0,1,0]))  # 2