"""
Given two strings, write a method to decide if one is a permutation of the other.
>>> is_permutation('abc', 'cab')
True

>>> is_permutation('aabb', 'abab')
True

>>> is_permutation('abcd', 'a')
False

>>> is_permutation('cable car', 'car bacle')
True

>>> is_permutation('title', 'music')
False

>>> is_permutation('kelly', 'kelly')
True
"""

def is_permutation(s1, s2):
    """Return true if two strings are permutations of each other."""

    if sorted(s1) == sorted(s2):
        return True

    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("PASSED ALL TESTS. ")