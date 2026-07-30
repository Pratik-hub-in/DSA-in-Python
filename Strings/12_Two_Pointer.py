"""
Program: Two Pointer Technique for Strings

Description:
The Two Pointer technique is an efficient algorithmic approach
used to solve string and array problems by maintaining two
pointers that move toward each other or in the same direction.

This program demonstrates two common applications:
1. Reverse a string.
2. Check if a string is a palindrome.

Time Complexity:
- Reverse String: O(n)
- Palindrome Check: O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand the Two Pointer technique.
- Learn efficient string manipulation.
- Compare characters from both ends of a string.
"""


def reverse_string(text: str) -> str:
    """
    Reverses a string using the Two Pointer technique.

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


def is_palindrome(text: str) -> bool:
    """
    Checks whether a string is a palindrome
    using the Two Pointer technique.

    The comparison ignores:
    - Uppercase and lowercase differences.
    - Spaces.
    - Special characters.

    Args:
        text (str): Input string.

    Returns:
        bool: True if palindrome, otherwise False.
    """
    filtered = [
        character.lower()
        for character in text
        if character.isalnum()
    ]

    left = 0
    right = len(filtered) - 1

    while left < right:
        if filtered[left] != filtered[right]:
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":

    text = "Data Structures"

    print("Original String:")
    print(text)

    print("\nReversed String:")
    print(reverse_string(text))

    palindrome_text = "A man, a plan, a canal: Panama"

    print("\nPalindrome Test:")
    print(palindrome_text)

    if is_palindrome(palindrome_text):
        print("Result: Palindrome")
    else:
        print("Result: Not a Palindrome")


# Key Takeaways:
# • Two Pointer is an efficient technique for many string problems.
# • It often avoids unnecessary nested loops.
# • Preprocessing simplifies palindrome checking.
# • This pattern is frequently used in coding interviews.
