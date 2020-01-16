"""
Unique values
>>> A = [12, 28, 46, 32, 50]
>>> B = [50, 12, 32, 46, 28]
>>> anagram_mapping(A, B)
[1, 4, 3, 2, 0]

Empty lists
>>> A = []
>>> B = []
>>> anagram_mapping(A, B)
[]

Repeating numbers
>>> A = [1, 2, 1]
>>> B = [2, 1, 1]
>>> anagram_mapping(A, B)
[2, 0, 1]
"""

def anagram_mapping(A, B):
    P = []
    indices_dict = {}
    for i, num in enumerate(B):
        indices = indices_dict.get(num, [])
        indices.append(i)
        indices_dict[num] = indices

    for num in A:
        index = indices_dict[num].pop()
        P.append(index)

    return P

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print ("All tests passed!")
