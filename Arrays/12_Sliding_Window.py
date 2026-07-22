"""
Program: Sliding Window Technique

Description:
The Sliding Window technique is used to solve problems involving
contiguous subarrays or substrings efficiently.

In this example, we find the maximum sum of any contiguous
subarray of size k.

Example:
Input:
Array = [2, 1, 5, 1, 3, 2]
k = 3

Subarrays:
[2, 1, 5] -> 8
[1, 5, 1] -> 7
[5, 1, 3] -> 9
[1, 3, 2] -> 6

Output:
Maximum Sum = 9

Algorithm:
1. Calculate the sum of the first k elements.
2. Store it as the current and maximum sum.
3. Slide the window one element at a time:
   - Add the incoming element.
   - Remove the outgoing element.
4. Update the maximum sum if needed.

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""


def maximum_sum_subarray(arr, k):
    """
    Returns the maximum sum of any contiguous
    subarray of size k.

    Args:
        arr (list[int]): Input array.
        k (int): Window size.

    Returns:
        int: Maximum subarray sum.
    """
    if k <= 0 or k > len(arr):
        raise ValueError("Window size must be between 1 and the length of the array.")

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    numbers = [2, 1, 5, 1, 3, 2]
    window_size = 3

    print("Array:", numbers)
    print("Window Size:", window_size)
    print("Maximum Sum:", maximum_sum_subarray(numbers, window_size))
