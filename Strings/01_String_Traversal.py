"""
Program: String Traversal

Description:
String traversal is the process of accessing each character of a
string one by one. Since strings are immutable in Python, their
characters cannot be modified directly.

This program demonstrates two common ways to traverse a string:
1. Using a for loop.
2. Using index-based traversal.

Example:
Input:
String = "Python"

Output:
P
y
t
h
o
n

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""


def traverse_using_loop(text):
    """
    Traverses a string using a for loop.

    Args:
        text (str): Input string.
    """
    print("Traversal using for loop:")

    for character in text:
        print(character)


def traverse_using_index(text):
    """
    Traverses a string using indexing.

    Args:
        text (str): Input string.
    """
    print("\nTraversal using index:")

    for index in range(len(text)):
        print(f"Index {index}: {text[index]}")


if __name__ == "__main__":
    text = "Python"

    print("Original String:", text)
    print()

    traverse_using_loop(text)
    traverse_using_index(text)
