def last_stone_weight(stones):
    stones.sort()

    while len(stones) > 1:
        stones.sort()
        if stones[-2] == stones[-1]:
            stones = stones[:-2]
        else:
            stones = stones[:-2] + [stones[-1] - stones[-2]]

    if not stones:
        return 0
    return stones[0]

print(last_stone_weight([2,7,4,1,8,1]))
print(last_stone_weight([3,8]))
print(last_stone_weight([0,0]))
print(last_stone_weight([]))