def restore_string(s, indices):
    """Return the unshuffled string."""
    d, l, res = {}, len(indices), ''

    for i in range(l):
        d[indices[i]] = s[i]

    for i in range(l):
        res += d[i]

    return res

print(restore_string('codeleet', [4,5,6,7,0,2,1,3]))  # leetcode
print(restore_string('abc', [0,1,2]))  # abc
print(restore_string('aaiougrt', [4,0,2,6,7,3,1,5]))  # arigatou