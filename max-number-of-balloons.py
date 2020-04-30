def max_balloons(text) -> int:
    """
    Return the number of instances of 'balloon'
    that can be formed with the given text.
    """
    b, t = {}, {}
    for c in 'balloon':
        b[c] = b.get(c, 0) + 1

    for c in text:
        t[c] = t.get(c, 0) + 1

    instances = float('inf')
    for c in b:
        instances = min(instances, t.get(c, 0))

    return instances


print(max_balloons("nlaebolko"))  # 1
print(max_balloons("loonbalxballpoon"))  # 2
print(max_balloons("leetcode"))  # 0
print(max_balloons(""))  # 0
