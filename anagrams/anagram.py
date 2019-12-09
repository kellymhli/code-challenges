"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:
    >>> import os, sys
    >>> all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""


def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""

    word_dict = {}

    for word in wordlist:
        alpha = ''.join(sorted(word))  # Alphabetize all letters in the word

        # Add word to list with alphabetized word as the key
        if word_dict.get(alpha) == None:
            word_dict[alpha] = [word]
        else:
            word_dict[alpha].append(word)

    most_ana_word = None  # Keep track of word with most anagrams
    max_ana = 0   # Keep track of longest list

    # Find the anagram with the longest list and get the first word alphabetically
    for word, lst in word_dict.items():
        if len(lst) > max_ana:
            max_ana = len(lst)
            most_ana_word = sorted(lst)[0]  # First word in the alphabetized list

    return most_ana_word


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
