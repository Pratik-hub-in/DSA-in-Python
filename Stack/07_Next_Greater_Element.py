"""
Program: Next Greater Element

Description:
This program finds the next greater element for every
element in an array using a Stack.

The next greater element of an element is the first element
to its right that is greater than it.

If no greater element exists, the result is -1.

Example:

Input:
[4, 5, 2, 10, 8]

Output:
[5, 10, 10, -1, -1]

Explanation:
4 -> 5
5 -> 10
2 -> 10
10 -> -1
8 -> -1

Brute Force Approach:
For every element, search all elements to its right.

Time Complexity:
- O(n²)

Optimized Stack Approach:
Traverse the array from right to left while maintaining
a decreasing stack.

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand the Next Greater Element problem.
- Learn the Monotonic Stack technique.
- Optimize an O(n²) solution to O(n).
"""


def next_greater_element(numbers: list[int]) -> list[int]:
    """
    Finds the next greater element for every array element.

    Args:
        numbers (list[int]): Input array.

    Returns:
        list[int]: Next greater element for each value.
    """
    result = [-1] * len(numbers)
    stack = []

    for index in range(len(numbers) - 1, -1, -1):

        while stack and stack[-1] <= numbers[index]:
            stack.pop()

        if stack:
            result[index] = stack[-1]

        stack.append(numbers[index])

    return result


if __name__ == "__main__":

    test_cases = [
        [4, 5, 2, 10, 8],
        [1, 3, 2, 4],
        [6, 5, 4, 3, 2, 1],
        [2, 2, 3, 1]
    ]

    for numbers in test_cases:

        result = next_greater_element(numbers)

        print(f"Input:  {numbers}")
        print(f"Output: {result}")
        print()


# Key Takeaways:
# • The next greater element must be to the right.
# • Traversing from right to left makes the problem easier.
# • Smaller or equal elements can be removed from the stack.
# • Each element is pushed and popped at most once.
# • Therefore, the optimized solution runs in O(n) time.
# • This is a fundamental Monotonic Stack pattern.
