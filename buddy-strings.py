def buddy_strings(A, B) -> bool:
    length = len(A)
    if length != len(B):
        return False

    seen, dup, diff = set(), False, []
    for i in range(length):
        if A[i] == B[i]:
            if A[i] in seen:
                dup = True
            else:
                seen.add(A[i])
        else:
            diff.append((A[i], B[i]))

    if len(diff) == 0:
        return dup
    elif len(diff) == 2:
        return diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]

    return False

print(buddy_strings("", "abc"))  #F
print(buddy_strings("aaabc", "aaacb"))  #T
print(buddy_strings("aa", "aa"))  #T
print(buddy_strings("ab", "ab"))  #F