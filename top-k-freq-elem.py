def getTopKElem(nums, k):
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1

    sorted_lst = [(k, d[k]) for k in d]
    sorted_lst.sort(key = lambda x: x[1])

    return [x[0] for x in sorted_lst[-k:]]

print(getTopKElem([1], 1))
print(getTopKElem([1,2,3,1,2,1,1,2], 2))