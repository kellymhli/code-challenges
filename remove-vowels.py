"""
>>> removeVowel("aeiou")
''

>>> removeVowel("abcdefgh")
'bcdfgh'

>>> removeVowel("")
''
"""


def removeVowel(S):
    """Return a S with all vowels removed."""

    alpha = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    new_str = ''
    for c in S:
        if c not in alpha:
            new_str += c
    return new_str

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("Tests passed.")

    stng = input("Your new String: ")
    print(removeVowel(stng))