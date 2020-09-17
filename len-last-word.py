def return_last_len(s):
    """Return the length of the last word in a string."""

    words = s.split()

    if not words:
        # No words in the string
        return 0

    return len(words[-1])

print(return_last_len(""))  # 0
print(return_last_len(" "))  # 0
print(return_last_len("abc"))  # 3
print(return_last_len("Return the length of the following words: Blubbers"))  # 8