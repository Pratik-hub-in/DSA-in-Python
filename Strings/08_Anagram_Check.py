"""
Program: Anagram Check

Description:
An anagram is a word or phrase formed by rearranging the letters
of another word or phrase using all the original letters exactly once.

This program demonstrates two methods to check whether two strings
are anagrams.

Method 1:
- Sort both strings and compare them.

Method 2:
- Compare character frequencies using a dictionary.

The program ignores:
- Uppercase and lowercase differences.
- Spaces.
- Special characters.

Example:
Input:
String 1 = "Listen"
String 2 = "Silent"

Output:
Strings are Anagrams.

Time Complexity:
- Sorting Method: O(n log n)
- Dictionary Method: O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Learn string preprocessing.
- Understand dictionary-based frequency counting.
- Compare two common approaches for solving anagram problems.
"""

import re


def clean_string(text: str) -> str:
    """
    Removes non-alphanumeric characters and converts
    the string to lowercase.

    Args:
        text (str): Input string.

    Returns:
        str: Cleaned string.
    """
    return re.sub(r"[^a-zA-Z0-9]", "", text).lower()


def is_anagram_sorting(first: str, second: str) -> bool:
    """
    Checks whether two strings are anagrams
    using the sorting approach.

    Args:
        first (str): First string.
        second (str): Second string.

    Returns:
        bool: True if anagrams, otherwise False.
    """
    first = clean_string(first)
    second = clean_string(second)

    return sorted(first) == sorted(second)


def is_anagram_dictionary(first: str, second: str) -> bool:
    """
    Checks whether two strings are anagrams
    using a character frequency dictionary.

    Args:
        first (str): First string.
        second (str): Second string.

    Returns:
        bool: True if anagrams, otherwise False.
    """
    first = clean_string(first)
    second = clean_string(second)

    if len(first) != len(second):
        return False

    frequency = {}

    for character in first:
        frequency[character] = frequency.get(character, 0) + 1

    for character in second:
        if character not in frequency:
            return False

        frequency[character] -= 1

        if frequency[character] < 0:
            return False

    return True


if __name__ == "__main__":
    first_string = "Listen"
    second_string = "Silent"

    print("First String :", first_string)
    print("Second String:", second_string)

    print("\nMethod 1: Using Sorting")
    print(
        "Strings are Anagrams"
        if is_anagram_sorting(first_string, second_string)
        else "Strings are Not Anagrams"
    )

    print("\nMethod 2: Using Dictionary")
    print(
        "Strings are Anagrams"
        if is_anagram_dictionary(first_string, second_string)
        else "Strings are Not Anagrams"
    )


# Key Takeaways:
# • Anagrams contain the same characters with the same frequencies.
# • Sorting is simple but takes O(n log n) time.
# • Dictionary-based frequency counting runs in O(n) time.
# • Preprocessing makes the program robust against case differences and spaces.
