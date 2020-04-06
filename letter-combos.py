def letter_combos(digits) -> list:
    if not digits:
        return []
    d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

    if len(digits) == 1:
        return [t for t in d.get(digits[0])]
    return [t + subs for t in d.get(digits[0]) for subs in letter_combos(digits[1:])]

print(letter_combos("23"))