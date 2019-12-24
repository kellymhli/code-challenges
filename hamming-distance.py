"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note: 0 <= x, y <= 2^31

>>> sol = Solution()
>>> sol.hammingDistance(1, 4)
2

>>> sol = Solution()
>>> sol.hammingDistance(1, 5)
1

>>> sol = Solution()
>>> sol.hammingDistance(1, 1)
0
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = bin(x).replace('0b', '')
        bin_y = bin(y).replace('0b', '')

        len_x = len(bin_x)
        len_y = len(bin_y)

        if len_x > len_y:
            longer = len_x
            bin_y = '0'*(longer - len_y) + bin_y
        else:
            longer = len_y
            bin_x = '0'*(longer - len_x) + bin_x

        diff = 0
        for i in range(0, longer):
            if bin_x[i] != bin_y[i]:
                diff += 1

        return diff


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('ALL TESTS PASSED')

    sol = Solution()
    x = int(input('x: '))
    y = int(input('y: '))
    print (sol.hammingDistance(x, y))