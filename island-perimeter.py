def islandPerimeter(grid):
    if len(grid) == 0:
        return 0

    def countPeri(grid, i, j):
        count = 0
        if (j-1 < 0 or grid[i][j-1] == 0):
            count += 1
        if (j+1 == len(grid[0]) or grid[i][j+1] == 0):
            count += 1
        if (i-1 < 0 or grid[i-1][j] == 0):
            count += 1
        if (i+1 == len(grid) or grid[i+1][j] == 0):
            count += 1
        return count

    peri = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                peri += countPeri(grid, i, j)
    return peri

print(islandPerimeter([]))
print(islandPerimeter([[1]]))
print(islandPerimeter([[0,1,0], [1,1,0], [0,0,0]]))