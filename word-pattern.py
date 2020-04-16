def get_pattern(iterable) -> list:
    """Generate pattern index array."""
    d, res = {}, []
    for i, item in enumerate(iterable):
        if item not in d:
            d[item] = i
        res += [d[item]]
    return res

def word_pattern(pattern, string) -> bool:
    """Determine if string follows the pattern."""
    string = string.split()
    return get_pattern(pattern) == get_pattern(string)

print(word_pattern('abba', 'dog cat cat dog'))  # True
print(word_pattern('abba', 'cat dog cat dog'))  # False
