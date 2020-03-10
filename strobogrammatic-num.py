"""
>>> is_strobogrammatic("88")
True

>>> is_strobogrammatic("52")
False

>>> is_strobogrammatic("1111")
True

"""

def is_strobogrammatic(num):
    """
    A Strobogrammatic number is a number that looks the same when rotated 180 degrees.
    Determines if num is strobogrammatic.
    """

    d = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    flipped_num = ""

    for n in num:
        match = d.get(n, None)
        if match == None:
            return False
        else:
            flipped_num += match

    return flipped_num[::-1] == num


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("ALL TESTS PASSED.")

    num = input("Enter a number: ")
    try:
        print(num, "is strobogrammatic: ", is_strobogrammatic(num))
    except:
        print("Exiting program.")
