def num_pairs_divisible_by_60(times) -> int:
    """Return number of pairs of songs have a total duration divisible by 60."""

    d = {}
    res = 0

    for i in range(len(times)):
        remainder = times[i] % 60
        if 60 - remainder in d:
            res += d[60 - remainder]
        elif remainder == 0:
            res += d.get(remainder, 0)
        d[remainder] = d.get(remainder, 0) + 1

    return res

print(num_pairs_divisible_by_60([30,20,150,100,40]))  # 3
print(num_pairs_divisible_by_60([60,60,60]))  # 3
print(num_pairs_divisible_by_60([]))  # 0
print(num_pairs_divisible_by_60([111,33,129,87,88,92]))  # 3
