def longestHappyPrefix(s):
    res = ""
    i = len(s) - 1
    while i > 0:
        if s[:i] == s[-i:]:
            res = s[:i]
            break
        i -= 1
    return res

print(longestHappyPrefix("level"))
print(longestHappyPrefix("ababab"))
print(longestHappyPrefix("leetcodeleet"))
print(longestHappyPrefix("a"))