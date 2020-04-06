def digitSum(n) -> int:
    sn, res = str(n), 0
    for c in sn:
        res += int(c)
    return res

def countLargestGroup(n) -> int:
    d = {}
    for i in range(1, n+1):
        sm = digitSum(i)
        d[sm] = d.get(sm, []) + [i]

    res, largest = 0, 0
    for lst in d.values():
        lst_len = len(lst)
        if lst_len > largest:
            res = 1
            largest = lst_len
        elif lst_len == largest:
            res += 1

    return res

print(countLargestGroup(13))  # 4
print(countLargestGroup(2))  # 2
print(countLargestGroup(15))  # 6