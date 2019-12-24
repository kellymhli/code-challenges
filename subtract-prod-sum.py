"""
>>> subtract_prod_sum(234)
15
>>> subtract_prod_sum(0)
0
"""
def subtract_prod_sum(n: int) -> int:

    if n == 0:
        return 0

    n_str = str(n)

    digit_prod = 1
    digit_sum = 0

    for num in n_str:
        digit_prod *= int(num)
        digit_sum += int(num)

    return (digit_prod - digit_sum)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('PASSED ALL TESTS')

    n = input('Enter a number: ').upper()
    while n != 'Q':
        print(subtract_prod_sum(n))
        n = input('Enter a number (or q to quit): ').upper()
