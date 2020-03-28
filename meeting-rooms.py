def can_attend_meetings(intervals):
    intervals.sort(key = lambda x: x[0])
    for i in range(len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            return False

    return True

print(can_attend_meetings([[7,10],[2,4]]))
print(can_attend_meetings([[0,30],[5,10],[15,20]]))
print(can_attend_meetings([[1,5]]))