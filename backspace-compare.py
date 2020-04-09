def make_stack(s) -> list:
    stack = []
    for c in s:
        if c == '#':
            if stack:
                stack.pop()
        else:
            stack += [c]
    return stack


def compare_str(s1, s2) -> bool:
    return make_stack(s1) == make_stack(s2)

print(compare_str("ab#c", "ad#c"))
print(compare_str("abc##", "acb#"))