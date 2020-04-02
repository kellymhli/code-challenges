def shiftGrid(grid, k):

    lst = []
    for row in grid:
        lst.extend(row)

    k = k % len(lst)
    lst = lst[-k:] + lst[:-k]

    start, end, row_len, res = 0, len(grid[0]), len(grid[0]), []
    while end <= len(lst):
        res.append(lst[start:end])
        start += row_len
        end += row_len

    return res

print(shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1))
print(shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9))
print(shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4))
print(shiftGrid([[1],[2],[3],[4],[7],[6],[5]], 23))