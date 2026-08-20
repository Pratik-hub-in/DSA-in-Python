"""
Program: First Non-Repeating Character

Description:
Given a string, find the first character that does not
repeat anywhere in the string.

A Queue is used to maintain the order in which characters
appear.

A frequency dictionary keeps track of how many times each
character occurs.

Example:

Input:
"swiss"

Frequency:
s -> 3
w -> 1
i -> 1

Processing order:
s -> repeated
w -> non-repeating

Output:
w

Approach:
1. Count the frequency of every character.
2. Traverse the string from left to right.
3. Add characters to the Queue.
4. Remove characters from the front while their frequency
   is greater than 1.
5. The character at the front is the first non-repeating
   character.

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand how Queue can be used in string problems.
- Learn frequency counting using a dictionary.
- Understand how FIFO preserves character order.
- Combine multiple data structures to solve a problem.
"""

from collections import deque, Counter


def first_non_repeating_character(text: str) -> str | None:
    """
    Finds the first non-repeating character in a string.

    Args:
        text (str): Input string.

    Returns:
        str | None: First non-repeating character.
                    Returns None if no such character exists.
    """

    if not text:
        return None

    # Count frequency of every character.
    frequency = Counter(text)

    # Queue stores characters in their original order.
    queue = deque()

    for character in text:

        queue.append(character)

        # Remove repeated characters from the front.
        while queue and frequency[queue[0]] > 1:
            queue.popleft()

    if queue:
        return queue[0]

    return None


if __name__ == "__main__":

    test_cases = [
        "swiss",
        "aabbc",
        "aabbcc",
        "programming",
        "leetcode",
        "abcabcde",
    ]

    for text in test_cases:

        result = first_non_repeating_character(text)

        print(f"Input: {text}")

        if result is None:
            print("First Non-Repeating Character: None")
        else:
            print(f"First Non-Repeating Character: {result}")

        print()


# Key Takeaways:
# • Counter is used to calculate character frequencies.
# • deque maintains characters in their original order.
# • Repeated characters are removed from the front.
# • The first remaining character is the answer.
# • Each character enters and leaves the Queue at most once.
# • Overall time complexity is O(n).
