def k_weakest_rows(mat, k) -> list:
    rows = [(sum(row), i) for i, row in enumerate(mat)]
    rows.sort(key = lambda x: x[0])

    return [i for sm, i in rows[:k]]

print(k_weakest_rows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))  #[2,0,3]