import random

class Array:
    def __init__(self, nums):
        self.original = nums

    def reset(self) -> list:
        return self.original

    def shuffle(self) -> list:
        """Return random shuffle of array."""
        temp = self.original[:]
        res = []
        for i in range(len(temp)):
            res.append(temp.pop(random.randint(0, len(temp)-1)))
        return res

arr = Array([1,2,3,4,5])
print(arr.reset())
print(arr.shuffle())
print(arr.reset())
print(arr.shuffle())
print(arr.shuffle())
