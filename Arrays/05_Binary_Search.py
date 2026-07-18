"""
Program: Binary Search

Description:
Binary Search is an efficient searching algorithm used to find an element
in a sorted array. It works by repeatedly dividing the search interval
into half until the target element is found or the search interval becomes empty.

Prerequisite:
The array must be sorted in ascending order.

Algorithm:
1. Initialize two pointers: left and right.
2. Find the middle element.
3. Compare the middle element with the target.
4. If the target matches, return its index.
5. If the target is smaller, search the left half.
6. If the target is larger, search the right half.
7. Repeat until the element is found or the search space is exhausted.

Time Complexity:
- Best Case: O(1)
- Average Case: O(log n)
- Worst Case: O(log n)

Space Complexity:
- O(1)
"""


def binary_search(arr, target):
    """
    Searches for a target element in a sorted array.

    Args:
        arr (list): Sorted list of elements.
        target (int): Element to search.

    Returns:
        int: Index of the target if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


numbers = [10, 20, 30, 40, 50, 60, 70, 80]
target = 50

result = binary_search(numbers, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
