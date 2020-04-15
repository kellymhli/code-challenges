def is_pali(s) -> bool:
    return s == s[::-1]

def valid_palindrome(s) -> bool:
    """Determine if a string is a palindrome given at most one deletion/"""
    if not s:
        return True

    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return is_pali(s[i+1:j+1]) or is_pali(s[i:j-1])
        i += 1
        j -= 1

    return True

print(valid_palindrome("aba"))  # T
print(valid_palindrome("abcd"))  # F
print(valid_palindrome(""))  # T
print(valid_palindrome("abcdba"))  # T