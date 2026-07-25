"""
Program: Palindrome Check

Description:
A palindrome is a word, phrase, or sequence that reads the same
forward and backward.

This program demonstrates two methods to check whether a string
is a palindrome.

Method 1:
- Reverse the string using slicing.

Method 2:
- Compare characters using the Two-Pointer technique.

The program also ignores:
- Uppercase and lowercase differences
- Spaces
- Special characters

Example:
Input:
"A man, a plan, a canal: Panama"

Output:
Palindrome

Time Complexity:
- Slicing Method: O(n)
- Two-Pointer Method: O(n)

Space Complexity:
- O(n)
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


def is_palindrome_slicing(text: str) -> bool:
    """
    Checks if a string is a palindrome using slicing.
    """
    cleaned = clean_string(text)
    return cleaned == cleaned[::-1]


def is_palindrome_two_pointers(text: str) -> bool:
    """
    Checks if a string is a palindrome using
    the Two-Pointer technique.
    """
    cleaned = clean_string(text)

    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    text = "A man, a plan, a canal: Panama"

    print("Original String:")
    print(text)

    print("\nMethod 1: Using Slicing")
    print("Palindrome" if is_palindrome_slicing(text) else "Not a Palindrome")

    print("\nMethod 2: Using Two Pointers")
    print("Palindrome" if is_palindrome_two_pointers(text) else "Not a Palindrome")


# Key Takeaways:
# • A palindrome reads the same forwards and backwards.
# • Preprocessing simplifies comparison.
# • The Two-Pointer technique avoids creating a reversed string.
