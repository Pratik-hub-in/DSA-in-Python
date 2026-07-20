"""
Program: Reverse an Array

Description:
This program demonstrates two methods to reverse an array:
1. Using Python slicing.
2. Using the Two-Pointer technique (in-place reversal).

Algorithm (Two-Pointer Method):
1. Initialize two pointers:
   - left at the beginning of the array.
   - right at the end of the array.
2. Swap the elements at the left and right pointers.
3. Move the left pointer one step forward.
4. Move the right pointer one step backward.
5. Repeat until the pointers meet.

Time Complexity:
- Slicing Method: O(n)
- Two-Pointer Method: O(n)

Space Complexity:
- Slicing Method: O(n)
- Two-Pointer Method: O(1)
"""


def reverse_using_slicing(arr):
    """
    Reverses an array using Python slicing.

    Args:
        arr (list): Input array.

    Returns:
        list: Reversed array.
    """
    return arr[::-1]


def reverse_using_two_pointers(arr):
    """
    Reverses an array in-place using the Two-Pointer technique.

    Args:
        arr (list): Input array.

    Returns:
        list: Reversed array.
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]

    print("Original Array:", numbers)

    print("\nMethod 1: Using Slicing")
    print(reverse_using_slicing(numbers))

    print("\nMethod 2: Using Two Pointers")
    print(reverse_using_two_pointers(numbers.copy()))
