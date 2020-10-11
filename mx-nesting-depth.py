def returnNestingDepth(s):
    """
    Return the max nesting depth of the s.
    Nesting depth = depth of a set of parentheses.
    """

    if len(s) <= 1:
        # No sets of parens possible
        return 0

    max_depth, op = 0, 0

    for c in s:
        if c == '(':
            # New paren set
            op += 1
            if op > max_depth:
                max_depth = op
        elif c == ')':
            # Closed paren set
            op -= 1

    return max_depth

print(returnNestingDepth('(())'))  # 2
print(returnNestingDepth('a'))  # 0
print(returnNestingDepth('('))  # 0
print(returnNestingDepth(''))  # 0
print(returnNestingDepth('(1+(2*3)+((8)/4))+1'))  # 3
print(returnNestingDepth('(1)+((2))+(((3)))'))  # 3
print(returnNestingDepth('1+(2*3)/(2-1)'))  # 1

