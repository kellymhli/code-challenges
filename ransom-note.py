"""
>>> canMakeRansom("", "")
True
>>> canMakeRansom("", "aabc")
True
>>> canMakeRansom("abc", "")
False
>>> canMakeRansom("aa", "aba")
True
>>> canMakeRansom("aab", "aac")
False
"""

def canMakeRansom(ransom, magazine):
    if ransom == magazine or not ransom:
        return True
    if not magazine:
        return False

    d = {}
    for c in magazine:
        d[c] = d.get(c, 0) + 1

    for c in ransom:
        val = d.get(c, 0)
        if val == 0:
            return False
        else:
            d[c] = val - 1
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("Passed all tests!\n")