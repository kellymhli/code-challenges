def reverse_string(s, k) -> str:
    """
    Given a string and an integer k, you need to reverse the first k characters
    for every 2k characters counting from the start of the string. If there are
    less than k characters left, reverse all of them. If there are less than 2k
    but greater than or equal to k characters, then reverse the first k characters
    and left the other as original.
    """

    res = ''
    i = 0
    while i < len(s):
        res += s[i : i + k][::-1] + s[i + k : i + 2 * k]
        i = i + 2 * k
    return res

print(reverse_string('abcdefg', 2))  #bacdfeg
print(reverse_string('abcdefg', 3))  #cbadefg
print(reverse_string('', 1))  # ''