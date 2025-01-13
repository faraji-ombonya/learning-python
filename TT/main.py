from collections import Counter


def minimum_anagram_size(s):
    """
    Calculate the minimum size of an anagram group.

    Args:
        s (str): Input string.

    Returns:
        int: Minimum size of an anagram group.
    """

    groups = []
    current_group = Counter()

    for char in s:
        current_group[char] += 1

        print(current_group)
    


print(minimum_anagram_size("abba"))       
print(minimum_anagram_size("ababaaaab"))
print(minimum_anagram_size("cdef"))   