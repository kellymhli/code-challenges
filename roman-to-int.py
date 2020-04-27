def roman_to_int(s) -> int:
    if not s:
        return 0

    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    prev, res = 0, 0
    for c in s:
        val = d.get(c)
        res += val
        if prev < val:
            res -= 2*prev
        prev = val
    return res

print(roman_to_int('III'))  #3
print(roman_to_int('IV'))  #4
print(roman_to_int(''))  #0