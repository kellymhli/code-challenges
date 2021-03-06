"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards(0)
    '0'

    >>> dec2bin_backwards(1)
    '1'

    >>> dec2bin_backwards(2)
    '10'

    >>> dec2bin_backwards(4)
    '100'

    >>> dec2bin_backwards(15)
    '1111'

# For example, using our alternate solution::

#     >>> dec2bin_forwards(0)
#     '0'

#     >>> dec2bin_forwards(1)
#     '1'

#     >>> dec2bin_forwards(2)
#     '10'

#     >>> dec2bin_forwards(4)
#     '100'

#     >>> dec2bin_forwards(15)
#     '1111'

# And finally, using division:

#     >>> dec2bin_division(0)
#     '0'

#     >>> dec2bin_division(1)
#     '1'

#     >>> dec2bin_division(2)
#     '10'

#     >>> dec2bin_division(4)
#     '100'

#     >>> dec2bin_division(15)
#     '1111'


"""


def dec2bin_backwards(num):
    """Convert a decimal number to binary representation."""

    if num == 0:
        return "0"

    bin_num = ""

    while num >= 0:
        if (num % 2) == 0:
            bin_num += "1"
            print(bin_num)
        else:
            bin_num += "0"
            print (bin_num)
        num -= (num//2)

    return bin_num


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
