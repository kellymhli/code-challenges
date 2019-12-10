"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    odd = False  # Set word as having even number of chars by default
    if len(word) % 2 != 0:
        odd = True  # Set word as having odd number of chars

    char_dict = {}

    # Count the number of occurances of each char in word
    for char in word:
        count = char_dict.get(char, 0)
        char_dict[char] = count + 1

    # Check how many chars have an odd count
    odd_count = 0
    for count in char_dict.values():
        if count % 2 != 0:
            odd_count += 1

    # Odd and only one char is odd, ir even and no chars odd
    if (odd and odd_count == 1) or (not odd and odd_count == 0):
        return True
    else:
        return False


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
