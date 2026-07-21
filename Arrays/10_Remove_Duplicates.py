"""
Program: Remove Duplicates from an Array

Description:
This program demonstrates two approaches to remove duplicate
elements from an array while preserving their original order.

Approach 1:
- Traverse the array.
- Add an element to a new list only if it is not already present.

Approach 2:
- Use a set to keep track of seen elements.
- Preserve the insertion order by appending unseen elements.

Example:
Input : [10, 20, 30, 20, 40, 10, 50]
Output: [10, 20, 30, 40, 50]

Time Complexity:
- Approach 1: O(n²)
- Approach 2: O(n)

Space Complexity:
- O(n)
"""


def remove_duplicates_basic(arr):
    """
    Removes duplicates using a simple loop.

    Args:
        arr (list): Input array.

    Returns:
        list: Array with duplicates removed.
    """
    unique = []

    for item in arr:
        if item not in unique:
            unique.append(item)

    return unique


def remove_duplicates_optimized(arr):
    """
    Removes duplicates using a set while preserving order.

    Args:
        arr (list): Input array.

    Returns:
        list: Array with duplicates removed.
    """
    seen = set()
    unique = []

    for item in arr:
        if item not in seen:
            seen.add(item)
            unique.append(item)

    return unique


if __name__ == "__main__":
    numbers = [10, 20, 30, 20, 40, 10, 50]

    print("Original Array:")
    print(numbers)

    print("\nUsing Basic Method:")
    print(remove_duplicates_basic(numbers))

    print("\nUsing Optimized Method:")
    print(remove_duplicates_optimized(numbers))
