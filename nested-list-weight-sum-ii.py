def calcNestedSum(nestedList):
    depth, d, res = 1, {}, 0
    while nestedList:
        curr, nxt = [], []
        for item in nestedList:
            if type(item) == int:
                curr.append(item)
            else:
                nxt.extend(item)
        d[depth] = curr
        nestedList = nxt
        depth += 1

    for dep, lst in d.items():
        res += (depth - dep) * sum(lst)
    
    return res

print(calcNestedSum([1]))
print(calcNestedSum([1, [1,2]]))
print(calcNestedSum([1, [2, 3], 4, [1, [1,2]]]))