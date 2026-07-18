"""
Program: Linear Search

Description:
Linear Search is a simple searching algorithm that checks each element
of the array one by one until the target element is found or the end
of the array is reached.

Algorithm:
1. Start from the first element.
2. Compare each element with the target value.
3. If a match is found, return its index.
4. If no match is found after checking all elements, return -1.

Time Complexity:
- Best Case: O(1)
- Average Case: O(n)
- Worst Case: O(n)

Space Complexity:
- O(1)
"""

def linear_search(arr, target):
    """
    Searches for a target element in the array.

    Args:
        arr (list): List of elements.
        target (int): Element to search.

    Returns:
        int: Index of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


numbers = [12, 45, 67, 23, 89, 10]
target = 23

result = linear_search(numbers, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
