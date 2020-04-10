def calculateTime(keyboard, word):
    if not word:
        return 0

    idx = {c: i for i, c in enumerate(keyboard)}
    time, curr, prev = 0, 0, 0

    for c in word:
        curr = idx[c]
        time += abs(curr - prev)
        prev = curr

    return time

print(calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))  # 4
print(calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode"))  # 73