"""
This algorithm determines if a string has all unique characters.

>>> all_unique('this is a string')
False

>>> all_unique('abc def')
True

>>> all_unique('')
True

>>> unique_set('')
True

>>> unique_set('this is another string')
False

>>> unique_set('a b c')
False

>>> unique_set('abcdefg')
True

"""

def all_unique(stng):
    """Return true if string contains all unique chars using built in func."""

    for c in stng:
        if stng.count(c) > 1:
            return False

    return True


def unique_set(stng):
    """Return true if string contains all unique chars."""

    char_set = set()
    for c in stng:
        # c is already in set, so this is the second instance of c
        if c in char_set:
            return False
        else:
            char_set.add(c)

    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("ALL TESTS PASSED.")
