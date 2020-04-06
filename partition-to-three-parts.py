def canPartitionToThree(lst) -> bool:
    sm = sum(lst)
    if sm % 3 != 0:
        return False

    curr_sm, target, count = 0, sm//3, 0
    for n in lst:
        curr_sm += n
        if curr_sm == target:
            curr_sm = 0
            count += 1

    return count >= 3

print(canPartitionToThree([1,2,3,6,-1,7]))  # True
print(canPartitionToThree([1,2]))  # False
print(canPartitionToThree([0,2,1,-6,6,-7,9,1,2,0,1]))  # True
print(canPartitionToThree([0,2,1,-6,6,7,9,-1,2,0,1]))  # False
print(canPartitionToThree([3,3,6,5,-2,2,5,1,-9,4]))  # True