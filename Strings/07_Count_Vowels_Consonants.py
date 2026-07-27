"""
Program: Count Vowels and Consonants

Description:
This program counts the number of vowels and consonants in a string.

The program:
- Ignores spaces.
- Ignores digits.
- Ignores special characters.
- Treats uppercase and lowercase letters equally.

Example:
Input:
"Hello World 123!"

Output:
Vowels     : 3
Consonants : 7

Time Complexity:
- O(n)

Space Complexity:
- O(1)

Learning Outcomes:
- Understand character classification.
- Learn string traversal.
- Practice conditional statements.
"""

def count_vowels_and_consonants(text: str) -> tuple[int, int]:
    """
    Counts the number of vowels and consonants.

    Args:
        text (str): Input string.

    Returns:
        tuple[int, int]: Number of vowels and consonants.
    """
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for character in text.lower():
        if character.isalpha():
            if character in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


if __name__ == "__main__":
    text = "Hello World 123!"

    vowels, consonants = count_vowels_and_consonants(text)

    print("Original String:")
    print(text)

    print("\nAnalysis")
    print("-" * 20)
    print(f"Vowels     : {vowels}")
    print(f"Consonants : {consonants}")


# Key Takeaways:
# • isalpha() checks whether a character is a letter.
# • Converting to lowercase simplifies comparisons.
# • Digits, spaces, and special characters are ignored.
# • Character classification is frequently used in interview problems.
