"""
Program: Reverse a String

Description:
This program demonstrates three different methods to reverse a string.

Method 1:
- Using Python slicing.

Method 2:
- Using a loop.

Method 3:
- Using the Two-Pointer technique.

Since strings are immutable in Python, the Two-Pointer method
first converts the string into a list of characters.

Example:
Input:
String = "Python"

Output:
Reversed String = "nohtyP"

Time Complexity:
- Slicing: O(n)
- Loop: O(n)
- Two-Pointer: O(n)

Space Complexity:
- O(n)
"""


def reverse_using_slicing(text):
    """
    Reverses a string using slicing.

    Args:
        text (str): Input string.

    Returns:
        str: Reversed string.
    """
    return text[::-1]


def reverse_using_loop(text):
    """
    Reverses a string using a loop.

    Args:
        text (str): Input string.

    Returns:
        str: Reversed string.
    """
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return reversed_text


def reverse_using_two_pointers(text):
    """
    Reverses a string using the Two-Pointer technique.

    Args:
        text (str): Input string.

    Returns:
        str: Reversed string.
    """
    characters = list(text)

    left = 0
    right = len(characters) - 1

    while left < right:
        characters[left], characters[right] = (
            characters[right],
            characters[left],
        )

        left += 1
        right -= 1

    return "".join(characters)


if __name__ == "__main__":
    text = "Python"

    print("Original String:", text)

    print("\nMethod 1: Using Slicing")
    print(reverse_using_slicing(text))

    print("\nMethod 2: Using Loop")
    print(reverse_using_loop(text))

    print("\nMethod 3: Using Two Pointers")
    print(reverse_using_two_pointers(text))


# Key Takeaways:
# • Strings are immutable in Python.
# • Slicing is the simplest and most Pythonic way to reverse a string.
# • The Two-Pointer technique is commonly used in DSA problems.
