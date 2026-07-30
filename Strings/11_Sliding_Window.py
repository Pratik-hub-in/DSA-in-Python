"""
Program: Longest Substring Without Repeating Characters

Description:
This program finds the length of the longest substring
without repeating characters using the Sliding Window technique.

The Sliding Window approach maintains a window of unique
characters by expanding and shrinking the window as needed.

Example:
Input:
"abcabcbb"

Output:
Longest Substring Length = 3
Substring = "abc"

Time Complexity:
- O(n)

Space Complexity:
- O(min(n, m))
where m is the size of the character set.

Learning Outcomes:
- Understand the Sliding Window technique.
- Learn efficient substring processing.
- Practice dictionary-based indexing.
"""


def longest_unique_substring(text: str) -> tuple[int, str]:
    """
    Finds the longest substring without repeating characters.

    Args:
        text (str): Input string.

    Returns:
        tuple[int, str]:
            Length of the longest substring and
            the substring itself.
    """
    last_seen = {}
    left = 0

    max_length = 0
    start_index = 0

    for right, character in enumerate(text):

        if character in last_seen and last_seen[character] >= left:
            left = last_seen[character] + 1

        last_seen[character] = right

        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length
            start_index = left

    return (
        max_length,
        text[start_index:start_index + max_length]
    )


if __name__ == "__main__":

    text = "abcabcbb"

    length, substring = longest_unique_substring(text)

    print("Original String:")
    print(text)

    print("\nLongest Unique Substring:")
    print(substring)

    print("\nLength:")
    print(length)


# Key Takeaways:
# • Sliding Window reduces unnecessary comparisons.
# • Dictionaries provide O(1) average lookup time.
# • Each character is processed at most twice.
# • This is one of the most common interview problems.
