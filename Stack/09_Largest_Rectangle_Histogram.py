"""
Program: Largest Rectangle in Histogram

Description:
Given an array of bar heights, find the area of the
largest rectangle that can be formed in the histogram.

Example:

Input:
[2, 1, 5, 6, 2, 3]

Output:
10

Explanation:

        6
    5   6
    5   6
    5   6       3
2   1   5   2   3

The largest rectangle has:
Height = 5
Width  = 2

Area = 5 * 2 = 10

Approach:
A Monotonic Increasing Stack is used to store indices
of bars whose heights are in increasing order.

When a smaller bar is encountered, previously stored bars
can no longer extend to the current position, so their
maximum rectangle areas are calculated.

A sentinel value of 0 is added at the end to ensure all
remaining bars are processed.

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Apply the Monotonic Stack pattern to a complex problem.
- Understand left and right boundaries of rectangles.
- Calculate maximum rectangle areas efficiently.
- Improve an O(n²) solution to O(n).
"""


def largest_rectangle_area(heights: list[int]) -> int:
    """
    Finds the largest rectangle area in a histogram.

    Args:
        heights (list[int]): Heights of histogram bars.

    Returns:
        int: Maximum rectangle area.
    """
    stack = []
    max_area = 0

    heights.append(0)

    for index, height in enumerate(heights):

        while stack and heights[stack[-1]] > height:

            top_index = stack.pop()
            current_height = heights[top_index]

            if stack:
                width = index - stack[-1] - 1
            else:
                width = index

            area = current_height * width
            max_area = max(max_area, area)

        stack.append(index)

    heights.pop()

    return max_area


if __name__ == "__main__":

    test_cases = [
        [2, 1, 5, 6, 2, 3],
        [2, 4],
        [6, 2, 5, 4, 5, 1, 6],
        [1, 1, 1, 1],
        [5]
    ]

    for heights in test_cases:

        result = largest_rectangle_area(heights.copy())

        print(f"Heights: {heights}")
        print(f"Largest Rectangle Area: {result}")
        print()


# Key Takeaways:
# • A Monotonic Increasing Stack stores indices of bars.
# • When a smaller bar appears, rectangle boundaries can be calculated.
# • The stack allows each bar to be pushed and popped at most once.
# • Therefore, the algorithm runs in O(n) time.
# • A sentinel 0 height ensures all remaining bars are processed.
# • This is one of the most important Monotonic Stack patterns.
