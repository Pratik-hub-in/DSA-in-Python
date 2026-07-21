"""
Program: Right Rotation of an Array

Description:
This program demonstrates how to rotate an array to the right by
a given number of positions (k).

In a right rotation, each element shifts one position to the right,
and the last element moves to the beginning of the array.

Example:
Input : [10, 20, 30, 40, 50], k = 2
Output: [40, 50, 10, 20, 30]

Algorithm:
1. Check if the array is empty.
2. Find the effective rotation count using:
      k = k % len(arr)
3. Divide the array into two parts.
4. Place the last k elements before the remaining elements.

Time Complexity:
- O(n)

Space Complexity:
- O(n)
"""


def right_rotate(arr, k):
    """
    Rotates an array to the right by k positions.

    Args:
        arr (list): Input array.
        k (int): Number of right rotations.

    Returns:
        list: Right rotated array.
    """
    if not arr:
        return arr

    k = k % len(arr)

    return arr[-k:] + arr[:-k]


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    rotations = 2

    print("Original Array :", numbers)
    print("Rotations      :", rotations)
    print("Right Rotated  :", right_rotate(numbers, rotations))
