"""
Program: Longest Common Prefix

Description:
This program finds the longest common prefix among a list of strings.

A common prefix is a sequence of characters that appears at the
beginning of every string in the list.

Method 1:
- Compare characters one by one using the first string.

Method 2:
- Sort the list and compare only the first and last strings.

Example:
Input:
["flower", "flow", "flight"]

Output:
"fl"

Time Complexity:
- Iterative Method: O(n × m)
- Sorting Method: O(n log n)

Space Complexity:
- O(1) (excluding sorting)

Learning Outcomes:
- Learn prefix comparison.
- Understand how sorting can simplify comparisons.
- Practice string traversal.
"""


def longest_common_prefix(strings: list[str]) -> str:
    """
    Finds the longest common prefix using
    character-by-character comparison.

    Args:
        strings (list[str]): List of input strings.

    Returns:
        str: Longest common prefix.
    """
    if not strings:
        return ""

    prefix = strings[0]

    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


def longest_common_prefix_sorted(strings: list[str]) -> str:
    """
    Finds the longest common prefix using sorting.

    Args:
        strings (list[str]): List of input strings.

    Returns:
        str: Longest common prefix.
    """
    if not strings:
        return ""

    strings = sorted(strings)

    first = strings[0]
    last = strings[-1]

    index = 0

    while (
        index < len(first)
        and index < len(last)
        and first[index] == last[index]
    ):
        index += 1

    return first[:index]


if __name__ == "__main__":
    words = ["flower", "flow", "flight"]

    print("Input Strings:")
    print(words)

    print("\nMethod 1: Iterative Comparison")
    print("Longest Common Prefix:", longest_common_prefix(words))

    print("\nMethod 2: Sorting")
    print("Longest Common Prefix:", longest_common_prefix_sorted(words))


# Key Takeaways:
# • The common prefix appears at the beginning of every string.
# • The iterative method compares prefixes directly.
# • The sorting method compares only the first and last strings.
# • Longest Common Prefix is a common coding interview problem.
