def distribute_candies(candies) -> int:
    """
    Caclulate the max number of kinds of candies person B can get
    such that person A and person B get the same number of candies.
    The length of the candies array is always even.
    """
    s = set(candies)
    half_candies, kinds = len(candies)//2, len(s)
    if kinds >= half_candies:
        return half_candies
    else:
        return kinds

print(distribute_candies([1,1,2,2,3,3]))  # 3
print(distribute_candies([1,1,2,3]))  # 2
print(distribute_candies([1,2,3,4,5,6]))  # 3
print(distribute_candies([]))  # 0
