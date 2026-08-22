"""
Program: Rotting Oranges

Description:
Given a grid containing oranges:

0 -> Empty cell
1 -> Fresh orange
2 -> Rotten orange

Every minute, a rotten orange makes its adjacent
fresh oranges rotten.

Adjacent means:
- Up
- Down
- Left
- Right

The goal is to find the minimum number of minutes
required for all fresh oranges to become rotten.

If some fresh oranges can never become rotten,
return -1.

Example:

Input:

[
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

Output:
4

Approach:
This problem is solved using Multi-Source BFS.

All initially rotten oranges are inserted into the Queue
at the beginning.

Then BFS processes all rotten oranges level by level.

Each BFS level represents one minute.

Time Complexity:
- O(rows × columns)

Space Complexity:
- O(rows × columns)

Learning Outcomes:
- Understand BFS using a Queue.
- Learn Multi-Source BFS.
- Solve grid-based problems.
- Understand level-order processing.
- Apply Queue concepts to a real-world problem.
"""

from collections import deque


def oranges_rotting(grid: list[list[int]]) -> int:
    """
    Finds the minimum time required for all fresh oranges
    to become rotten.

    Args:
        grid (list[list[int]]): Grid containing 0, 1 and 2.

    Returns:
        int:
            Minimum number of minutes.
            -1 if some fresh oranges cannot become rotten.
    """

    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    columns = len(grid[0])

    queue = deque()

    fresh_oranges = 0

    # Add all initially rotten oranges to the Queue.
    for row in range(rows):

        for column in range(columns):

            if grid[row][column] == 2:
                queue.append((row, column))

            elif grid[row][column] == 1:
                fresh_oranges += 1

    # No fresh oranges exist.
    if fresh_oranges == 0:
        return 0

    minutes = 0

    # Four possible directions.
    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    while queue and fresh_oranges > 0:

        # Process one BFS level.
        level_size = len(queue)

        for _ in range(level_size):

            row, column = queue.popleft()

            for row_change, column_change in directions:

                new_row = row + row_change
                new_column = column + column_change

                # Check whether the new position is valid.
                if (
                    0 <= new_row < rows
                    and 0 <= new_column < columns
                    and grid[new_row][new_column] == 1
                ):

                    # Make the fresh orange rotten.
                    grid[new_row][new_column] = 2

                    fresh_oranges -= 1

                    queue.append((new_row, new_column))

        # One complete BFS level represents one minute.
        minutes += 1

    # If fresh oranges remain, they cannot be reached.
    if fresh_oranges > 0:
        return -1

    return minutes


if __name__ == "__main__":

    test_cases = [
        [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ],

        [
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]
        ],

        [
            [0, 2],
            [2, 0]
        ],

        [
            [1, 1],
            [1, 1]
        ]
    ]

    for index, grid in enumerate(test_cases, start=1):

        result = oranges_rotting(
            [row.copy() for row in grid]
        )

        print(f"Test Case {index}:")
        print(f"Minimum Minutes: {result}")
        print()


# Key Takeaways:
# • BFS is naturally implemented using a Queue.
# • All initially rotten oranges are starting points.
# • This is called Multi-Source BFS.
# • Each BFS level represents one minute.
# • A fresh orange is added to the Queue after becoming rotten.
# • If fresh oranges remain after BFS, return -1.
# • Time complexity is O(rows × columns).
