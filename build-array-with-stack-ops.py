def build_array(target) -> list:
    ops = []
    last = target[-1]
    target = set(target)
    for n in range(1, last+1):
        ops += ['Push']
        if n not in target:
            ops += ['Pop']
    return ops

print(build_array([1,3]))  # [Push, Push, Pop, Push]
print(build_array([1,2,3]))  # [Push, Push, Push]