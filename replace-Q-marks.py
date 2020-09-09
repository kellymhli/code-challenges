def replace_question_marks(s):
    """
    Replace all question marks in a string such
    that there are no consecutive repeating characters.
    """

    if len(s) <= 1:
        if s == '?':
            return a
        else:
            return s

    letters = 'abcdefghijklmnopqrstucvwxyz'
    l = len(letters)
    res = ''

    # Account for strings starting with '?'
    if s[0] == '?':
        for j in range(l):  # 26 letters in alphabet
            if s[1] != letters[j]:
                res += letters[j]
                break
    else:
        res += s[0]

    for i in range(1, len(s)-1):
        if s[i] == '?':
            for j in range(l):
                if letters[j] != res[-1] and letters[j] != s[i+1]:
                    res += letters[j]
                    break
        else:
            res += s[i]

    # Account for strings ending with '?'
    if s[-1] == '?':
        for j in range(l):
            if letters[j] != res[-1]:
                res += letters[j]
                break
    else:
        res += s[-1]

    return res


print(replace_question_marks('?ab'))  # bab
print(replace_question_marks('ubv?w'))  # ubvaw
print(replace_question_marks('??????'))  #ababab