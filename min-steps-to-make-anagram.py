def min_steps(s, t):
    """Calculate the minimum number of changes to t needed to make it an anagram of s."""
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1

    for c in t:
        if d.get(c, 0) > 0:
            d[c] -= 1

    return sum(d.values())

print(min_steps('abb', 'bab'))  #0
print(min_steps('abc', 'aab'))  #1
print(min_steps('leetcode', 'practice'))  #5