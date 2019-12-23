"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""


def one_off(lrg, sm):
    """Check if smaller word is one off of larger word."""

    diff = 0

    # Only need to add a char on front or end of smaller word
    if sm == lrg[0:-1] or sm == lrg[1:]:
        return True
    # If mismatch in middle of word, see if remaining characters match
    for i in range(0, len(sm)):
        if sm[i] != lrg[i]:
            return sm[i:] == lrg[i+1:]
    return False



def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""

    # Words are the same
    if w1 == w2:
        return True

    length_diff = len(w1) - len(w2)
    diff = 0  # Keep track of differences b/w the strings

    # w1 is one character off of w2
    if length_diff == -1:
        return one_off(w2, w1)
    elif length_diff == 1:
        return one_off(w1, w2)
    # Compare words of same length
    elif length_diff == 0:
        for i in range(0, len(w1)):
            if w1[i] != w2[i]:
                diff += 1
            if diff > 1:
                return False
        if diff <= 1:
            return True
    else:
        return False  # More than 1 edit needs to be made


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
