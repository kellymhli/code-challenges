import random
class Solution(object):
    def __init__(self, nums):
        self.num_dict = {}
        for i, num in enumerate(nums):
            lst = self.num_dict.get(num, [])
            lst.append(i)
            self.num_dict[num] = lst

    def pick(self, target):
        lst = self.num_dict[target]
        return lst[random.randint(0, len(lst) - 1)]

obj = Solution([1,2,3,3,3])
res = obj.pick(3)
print(res)