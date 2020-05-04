def reverseVowels(s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        v_order = []
        for c in s:
            if c in vowels:
                v_order += [c]

        res = ''
        for c in s:
            if c in vowels:
                res += v_order.pop()
            else:
                res += c
        return res

print(reverseVowels('hello'))  # holle
print(reverseVowels('leetcode'))  # leotcede