def replace_words(dict, s):
    dict = set(dict)
    words = s.split()
    res = ''

    for word in words:
        added = False
        for i in range(len(word)):
            if word[:i] in dict:
                res += ' ' + word[:i]
                added = True
                break
        if not added:
            res += ' ' + word

    return res[1:]

print(replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery"))