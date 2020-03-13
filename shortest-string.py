"""
>>> shortest_string("every breath you take, every move you make, i'll stand by you", 'boom')
'every breath you take, every move you make,'

"""

def shortest_string(s1, s2):
    if len(s2) > len(s1):
        return -1

    words = s1.split()
    res_lst = []
    pointer = 0
    for word in words:
        if pointer == len(s2):
            break
        if s2[pointer] in word:
            pointer += 1
        res_lst.append(word)
    return ' '.join(res_lst)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("ALL TESTS PASSED.")