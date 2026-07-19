"""
Program: Find Maximum and Minimum in an Array

Description:
This program finds the largest and smallest elements in an array by
traversing it only once.

Algorithm:
1. Initialize both maximum and minimum with the first element.
2. Traverse the remaining elements.
3. If the current element is greater than the maximum, update the maximum.
4. If the current element is smaller than the minimum, update the minimum.
5. Display the final maximum and minimum values.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)

Space Complexity:
- O(1)
"""


def find_max_min(arr):
    """
    Finds the maximum and minimum elements in an array.

    Args:
        arr (list): List of numbers.

    Returns:
        tuple: (maximum, minimum)
    """
    if not arr:
        return None

    maximum = arr[0]
    minimum = arr[0]

    for num in arr[1:]:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return maximum, minimum


numbers = [25, 12, 89, 43, 7, 65, 100, 18]

maximum, minimum = find_max_min(numbers)

print("Array:", numbers)
print("Maximum Element:", maximum)
print("Minimum Element:", minimum)
