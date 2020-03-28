def simplify_path(current, cd):
    path = current + '/' + cd
    dirs = path.split('/')
    stack = []
    for d in dirs:
        if d == '..':
            if stack:
                stack.pop()
        elif d == '.' or d == '':
            continue
        else:
            stack.append(d)
    res = '/' + '/'.join(stack)
    return res

print(simplify_path('/', '/facebook'))
print(simplify_path('facebook/anin', '../abc/def'))
print(simplify_path('/facebook/instagram', '../../../../.'))