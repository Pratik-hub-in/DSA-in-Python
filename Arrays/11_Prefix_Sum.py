"""
Program: Prefix Sum

Description:
This program demonstrates how to construct a Prefix Sum array.

A Prefix Sum array stores the cumulative sum of elements from the
beginning of the array up to each index.

Using a Prefix Sum array allows efficient calculation of the sum
of any subarray in constant time after preprocessing.

Example:
Input:
Array = [2, 4, 6, 8, 10]

Prefix Sum:
[2, 6, 12, 20, 30]

Sum of elements from index 1 to 3:
20 - 2 = 18

Time Complexity:
- Building Prefix Sum: O(n)
- Range Sum Query: O(1)

Space Complexity:
- O(n)
"""


def build_prefix_sum(arr):
    """
    Builds and returns the prefix sum array.

    Args:
        arr (list[int]): Input array.

    Returns:
        list[int]: Prefix sum array.
    """
    if not arr:
        return []

    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


def range_sum(prefix, left, right):
    """
    Returns the sum of elements between
    index left and right (inclusive).

    Args:
        prefix (list[int]): Prefix sum array.
        left (int): Starting index.
        right (int): Ending index.

    Returns:
        int: Sum of the specified range.
    """
    if left == 0:
        return prefix[right]

    return prefix[right] - prefix[left - 1]


if __name__ == "__main__":
    numbers = [2, 4, 6, 8, 10]

    prefix = build_prefix_sum(numbers)

    print("Original Array:")
    print(numbers)

    print("\nPrefix Sum Array:")
    print(prefix)

    left = 1
    right = 3

    print(f"\nSum from index {left} to {right}:")
    print(range_sum(prefix, left, right))
