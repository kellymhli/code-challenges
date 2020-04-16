def rm_min_paren(s) -> str:
    """Remove the minimum number of parentheses to make valid pairs."""
    par, res = 0, []
    for c in s:
        if c != ')':
            if c == '(':
                par += 1
            res += [c]
        elif par > 0:
            res += [c]
            par -= 1

    i = -1
    while par > 0:
        if res[i] == '(':
            res.pop(i)
            par -= 1
        else:
            i -= 1

    return ''.join(res)

print(rm_min_paren("))(("))  # ""
print(rm_min_paren("lee(t(c)o)de)"))  # "lee(t(c)o)de"
print(rm_min_paren("a)b(c)d"))  # "ab(c)d"