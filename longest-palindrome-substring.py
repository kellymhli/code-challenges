def expand_from_mid(s, l, r):
    if not s or l > r:
        return 0

    while l >=0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1

def longestPali(s):
    if not s or len(s) == 0:
        return s

    start, end = 0, 0
    for i in range(len(s)):
        l1 = expand_from_mid(s, i, i)
        l2 = expand_from_mid(s, i, i+1)
        l = max(l1, l2)
        if l > end - start:
            start = i - (l-1)//2
            end = i + l//2
    return s[start : end+1]

print(longestPali(""))
print(longestPali("a"))
print(longestPali("aa"))
print(longestPali("abcdcab"))
print(longestPali("racecar"))
print(longestPali("this is not a palindrome"))