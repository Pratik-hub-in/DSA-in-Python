"""
Program: Find the Length of a String

Description:
This program demonstrates two methods to determine the length of a string.

Method 1:
- Using Python's built-in len() function.

Method 2:
- Counting the characters manually using a loop.

Example:
Input:
String = "Python"

Output:
Length using len()    : 6
Length using loop     : 6

Time Complexity:
- Using len()      : O(1)
- Manual Counting  : O(n)

Space Complexity:
- O(1)
"""


def length_using_len(text):
    """
    Returns the length of a string using Python's built-in function.

    Args:
        text (str): Input string.

    Returns:
        int: Length of the string.
    """
    return len(text)


def length_using_loop(text):
    """
    Returns the length of a string by counting characters manually.

    Args:
        text (str): Input string.

    Returns:
        int: Length of the string.
    """
    count = 0

    for _ in text:
        count += 1

    return count


if __name__ == "__main__":
    text = "Python"

    print("Original String:", text)

    print("\nMethod 1: Using len()")
    print("Length:", length_using_len(text))

    print("\nMethod 2: Manual Counting")
    print("Length:", length_using_loop(text))
