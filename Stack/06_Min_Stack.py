"""
Program: Min Stack

Description:
A Min Stack is a Stack that supports normal stack operations
along with retrieving the minimum element in O(1) time.

Supported Operations:
1. Push
2. Pop
3. Top
4. Get Minimum

Example:

Push: 5
Push: 3
Push: 7
Push: 2

Stack:
Top -> 2
       7
       3
       5

Minimum:
2

After Pop:
Top -> 7
       3
       5

Minimum:
3

Approach:
Two stacks are used:
1. Main Stack  - stores all elements.
2. Min Stack   - stores the minimum value at each level.

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Top: O(1)
- Get Minimum: O(1)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand how auxiliary stacks can solve a problem efficiently.
- Learn to maintain the minimum value during stack operations.
- Practice O(1) time complexity for multiple operations.
"""


class MinStack:
    """
    Stack supporting constant-time minimum retrieval.
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, data: int) -> None:
        """
        Adds an element to the stack.

        Args:
            data (int): Value to be inserted.
        """
        self.stack.append(data)

        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self) -> int | None:
        """
        Removes and returns the top element.

        Returns:
            int | None: Removed element, or None if empty.
        """
        if not self.stack:
            print("Stack Underflow: Stack is empty.")
            return None

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def top(self) -> int | None:
        """
        Returns the top element without removing it.

        Returns:
            int | None: Top element, or None if empty.
        """
        if not self.stack:
            print("Stack is empty.")
            return None

        return self.stack[-1]

    def get_min(self) -> int | None:
        """
        Returns the minimum element in O(1) time.

        Returns:
            int | None: Minimum element, or None if empty.
        """
        if not self.min_stack:
            print("Stack is empty.")
            return None

        return self.min_stack[-1]

    def is_empty(self) -> bool:
        """
        Checks whether the stack is empty.

        Returns:
            bool: True if empty, otherwise False.
        """
        return len(self.stack) == 0

    def display(self) -> None:
        """
        Displays the main stack from top to bottom.
        """
        if self.is_empty():
            print("Stack is empty.")
            return

        print("Top")

        for value in reversed(self.stack):
            print(value)

        print("Bottom")


if __name__ == "__main__":

    stack = MinStack()

    print("Pushing elements:")

    for value in [5, 3, 7, 2, 8]:
        stack.push(value)

    stack.display()

    print("\nTop Element:")
    print(stack.top())

    print("\nMinimum Element:")
    print(stack.get_min())

    print("\nPopped Element:")
    print(stack.pop())

    print("\nMinimum Element After Pop:")
    print(stack.get_min())

    print("\nPopped Element:")
    print(stack.pop())

    print("\nMinimum Element After Pop:")
    print(stack.get_min())


# Key Takeaways:
# • A second stack is used to track minimum values.
# • get_min() runs in O(1) time.
# • The minimum stack is updated whenever a smaller or equal value is pushed.
# • Duplicate minimum values are handled correctly.
# • Push, Pop, Top, and Get Minimum all run in O(1) time.
