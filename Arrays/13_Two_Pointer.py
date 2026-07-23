"""
Program: Two Pointer Technique

Description:
The Two Pointer Technique is an efficient approach used to solve
array and string problems by maintaining two pointers that move
towards each other or in the same direction.

In this example, we check whether a sorted array contains two
elements whose sum is equal to a given target.

Example:
Input:
Array = [2, 5, 7, 11, 15]
Target = 18

Output:
Pair Found: (7, 11)

Algorithm:
1. Initialize two pointers:
   - left at the beginning of the array.
   - right at the end of the array.
2. Calculate the sum of the two elements.
3. If the sum equals the target, return the pair.
4. If the sum is smaller than the target, move the left pointer forward.
5. If the sum is greater than the target, move the right pointer backward.
6. Repeat until the pointers meet.

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""


def find_pair_with_sum(arr, target):
    """
    Finds two numbers in a sorted array whose sum equals the target.

    Args:
        arr (list[int]): Sorted input array.
        target (int): Target sum.

    Returns:
        tuple | None: Pair of numbers if found, otherwise None.
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return None


if __name__ == "__main__":
    numbers = [2, 5, 7, 11, 15]
    target = 18

    result = find_pair_with_sum(numbers, target)

    print("Array :", numbers)
    print("Target:", target)

    if result:
        print("Pair Found:", result)
    else:
        print("No valid pair found.")
