"""
Program: Stack Using Python List

Description:
A Stack is a linear data structure that follows the
LIFO (Last In, First Out) principle.

The element inserted last is the first element removed.

Example:

Push:
10
20
30

Stack:
30 <- Top
20
10

Pop:
30 is removed.

This implementation uses Python's built-in list.

Operations:
1. Push
2. Pop
3. Peek
4. Check if Empty
5. Display

Time Complexity:
- Push: O(1) amortized
- Pop: O(1)
- Peek: O(1)
- is_empty: O(1)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand the Stack data structure.
- Learn the LIFO principle.
- Implement basic stack operations.
- Understand how Python lists can be used as stacks.
"""


class Stack:
    """
    Represents a Stack using a Python list.
    """

    def __init__(self):
        self.items = []

    def push(self, data: int) -> None:
        """
        Adds an element to the top of the stack.

        Args:
            data (int): Value to be inserted.
        """
        self.items.append(data)

    def pop(self) -> int | None:
        """
        Removes and returns the top element.

        Returns:
            int | None: Removed element, or None if the stack is empty.
        """
        if self.is_empty():
            print("Stack Underflow: Stack is empty.")
            return None

        return self.items.pop()

    def peek(self) -> int | None:
        """
        Returns the top element without removing it.

        Returns:
            int | None: Top element, or None if the stack is empty.
        """
        if self.is_empty():
            print("Stack is empty.")
            return None

        return self.items[-1]

    def is_empty(self) -> bool:
        """
        Checks whether the stack is empty.

        Returns:
            bool: True if empty, otherwise False.
        """
        return len(self.items) == 0

    def display(self) -> None:
        """
        Displays the stack from top to bottom.
        """
        if self.is_empty():
            print("Stack is empty.")
            return

        print("Top")

        for item in reversed(self.items):
            print(item)

        print("Bottom")


if __name__ == "__main__":

    stack = Stack()

    print("Pushing elements:")
    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.display()

    print("\nTop Element:")
    print(stack.peek())

    print("\nPopped Element:")
    print(stack.pop())

    print("\nStack After Pop:")
    stack.display()

    print("\nIs Stack Empty?")
    print(stack.is_empty())


# Key Takeaways:
# • Stack follows the LIFO principle.
# • The last inserted element is removed first.
# • Python lists provide efficient append() and pop() operations.
# • peek() returns the top element without removing it.
# • Stack Underflow occurs when pop() is attempted on an empty stack.
