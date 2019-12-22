"""
>>> urlify('Mr John Smith   ', 13)
'Mr%20John%20Smith'

>>> urlify('hello', 5)
'hello'

>>> urlify('', 0)
''

"""

def urlify(stng, ln):
    """Return the url version of a string."""

    url = ''
    i = 0

    while i < ln:
        if stng[i] == ' ':
            url += '%20'
        else:
            url += stng[i]
        i += 1

    return url


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("ALL TESTS PASSED.")