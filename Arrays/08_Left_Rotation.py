"""
Program: Left Rotation of an Array

Description:
This program demonstrates how to rotate an array to the left by
a given number of positions (k).

In a left rotation, each element shifts one position to the left,
and the first element moves to the end of the array.

Example:
Input : [10, 20, 30, 40, 50], k = 2
Output: [30, 40, 50, 10, 20]

Algorithm:
1. Find the effective rotation count using:
      k = k % len(arr)
2. Divide the array into two parts.
3. Place the second part before the first part.

Time Complexity:
- O(n)

Space Complexity:
- O(n)
"""


def left_rotate(arr, k):
    """
    Rotates an array to the left by k positions.

    Args:
        arr (list): Input array.
        k (int): Number of left rotations.

    Returns:
        list: Left rotated array.
    """
    if not arr:
        return arr

    k = k % len(arr)

    return arr[k:] + arr[:k]


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    rotations = 2

    print("Original Array :", numbers)
    print("Rotations      :", rotations)
    print("Left Rotated   :", left_rotate(numbers, rotations))
