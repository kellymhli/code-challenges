def check_straight_line(coords) -> bool:
    if len(coords) < 2:
        return False
    if len(coords) == 2:
        return True
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    for x3, y3 in coords[2:]:
        if (y2-y1)*(x3-x1) != (y3-y1)*(x2-x1):
            return False
    return True

print(check_straight_line([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]))  # false
print(check_straight_line([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))  # True
print(check_straight_line([[1,1]]))  # False
print(check_straight_line([[1,1], [2,1]]))  # True