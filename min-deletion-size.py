"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete
all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices
{0, 2, 3}, then the final array after deletions is ["bef", "vyz"], and the
remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].
(Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)

Suppose we chose a set of deletion indices D such that after deletions, each
remaining column in A is in non-decreasing sorted order.

Return the minimum possible value of D.length.

    >>> min_del_size(['cba', 'daf', 'ghi'])
    1

    >>> min_del_size([])
    0

    >>> min_del_size(['a', 'b'])
    0

    >>> min_del_size(['aaa', 'ccc', 'bbb'])
    3

"""

def min_del_size(A):

    # Base case
    if len(A) == 0:
        return 0

    matrix = []
    dels = 0

    # Create list of lists of chars in each column
    i = 0
    while i < len(A[0]):
        new_lst = []
        for word in A:
            new_lst.append(word[i])
        matrix.append(new_lst)
        i += 1

    # Determine if a column is sorted or not
    for idx, lst in enumerate(matrix):
        if sorted(lst) != lst:
            dels += 1

    return dels


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("All tests passed!")