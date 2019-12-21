"""

>>> merge_sort([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]

>>> merge_sort([1, 5, 2, 6, 7, 8, 3, 4])
[1, 2, 3, 4, 5, 6, 7, 8]

>>> merge_sort([1, 5, 2, 6, 7, 8, 3, 4, 9])
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> merge_sort([])
[]
"""

def merge_sort(lst):
    """Sort an unsorted list recursively."""

    def merge(left, right):
        sort_lst = []

        l = 0
        r = 0

        # Iterate through lists and append smaller value to sorted list
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                sort_lst.append(left[l])
                l += 1
            else:
                sort_lst.append(right[r])
                r += 1

        # Add list to sorted list if the other is empty
        sort_lst += left[l:]
        sort_lst += right[r:]

        return sort_lst


    if len(lst) <= 1:
        return lst

    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\nALL TESTS PASSES!")