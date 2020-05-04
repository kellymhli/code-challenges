def destCity(paths) -> str:
    d = {}
    for a, b in paths:
        d[a] = b

    for a, b in paths:
        path = a
        while path in d:
            path = d[path]
        return path

print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))  # San Pablo
print(destCity([["B","C"],["D","B"],["C","A"]]))  # A
print(destCity([["A", "Z"]]))  # Z