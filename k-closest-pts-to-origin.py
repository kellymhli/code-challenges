def get_points(points, k) -> list:
    distances = []
    for x, y in points:
        distances += [(x*x + y*y, [x,y])]

    distances.sort(key = lambda x : x[0])
    return [x[1] for x in distances[:k]]

print(get_points([[1,3],[-2,2]], 1))  # [[-2, 2]]
print(get_points([[3,3],[5,-1],[-2,4]], 2))  # [[3,3],[-2,4]]