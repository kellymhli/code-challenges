def shift_string(s, shifts):
    if not shifts:
        return s

    move = 0
    for shift in shifts:
        if shift[0] == 0:  #left
            move -= shift[1]
        else:
            move += shift[1]
    move %= len(s)

    if move < 0:
        s = s[move:] + s[:-move + 1]
    elif move > 0:
        s = s[-move:] + s[:-move]
    return s

print(shift_string("abc", [[0,1], [1,2]]))  # cab
print(shift_string("acbdefg", [[1,1],[1,1],[0,2],[1,3]]))  #efgabcd
print(shift_string("mecsk", [[1,4],[0,5],[0,4],[1,1],[1,5]]))  # kmecs