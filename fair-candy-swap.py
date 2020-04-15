def fair_candy_swap(A, B):
    sum_a, sum_b = sum(A), sum(B)
    even = (sum_a + sum_b)//2
    needed_a = even - sum_a
    set_b = set(B)

    for a in A:
        if needed_a + a in set_b:
            return [a, needed_a + a]

    return None


print(fair_candy_swap([1,1], [2,2]))  # [1,2]
print(fair_candy_swap([1,2,5], [2,4]))  # [5,4]