def calculate_boats(people, limit):
    if not people:
        return 0

    boats, l, r = 0, 0, len(people) - 1
    people.sort()

    while l <= r:
        boats += 1
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1

    return boats

print(calculate_boats([3,3,4], 4))  # 3
print(calculate_boats([1,2], 3))  # 1
print(calculate_boats([], 4))