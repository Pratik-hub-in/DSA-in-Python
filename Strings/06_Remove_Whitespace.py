"""
Program: Remove Whitespace from a String

Description:
This program demonstrates two methods to remove whitespace from a string.

Method 1:
- Remove all whitespace characters.

Method 2:
- Remove extra spaces while preserving a single space
  between words.

Example:
Input:
"  Python   is   awesome!  "

Output:
Remove All Spaces:
"Pythonisawesome!"

Remove Extra Spaces:
"Python is awesome!"

Time Complexity:
- Method 1: O(n)
- Method 2: O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand different types of whitespace.
- Learn Python string manipulation techniques.
- Compare split()/join() and replace() methods.
"""

import re


def remove_all_whitespace(text: str) -> str:
    """
    Removes all whitespace characters from a string.

    Args:
        text (str): Input string.

    Returns:
        str: String without whitespace.
    """
    return re.sub(r"\s+", "", text)


def remove_extra_spaces(text: str) -> str:
    """
    Removes leading, trailing, and extra spaces while
    preserving a single space between words.

    Args:
        text (str): Input string.

    Returns:
        str: Cleaned string.
    """
    return " ".join(text.split())


if __name__ == "__main__":
    text = "  Python   is   awesome!  "

    print("Original String:")
    print(f'"{text}"')

    print("\nMethod 1: Remove All Whitespace")
    print(f'"{remove_all_whitespace(text)}"')

    print("\nMethod 2: Remove Extra Spaces")
    print(f'"{remove_extra_spaces(text)}"')


# Key Takeaways:
# • Whitespace includes spaces, tabs, and newline characters.
# • re.sub() is useful for pattern-based replacements.
# • split() + join() is a simple way to normalize spaces.
