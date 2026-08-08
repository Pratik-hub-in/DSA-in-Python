"""
Program: Stack Using Linked List

Description:
This program implements a Stack using a Singly Linked List.

A Stack follows the LIFO (Last In, First Out) principle.

In this implementation:
- Push operation inserts a node at the beginning.
- Pop operation removes the node from the beginning.
- Peek operation returns the top element.
- No Python list is used for storing stack elements.

Example:

Push 10:
Top -> 10 -> None

Push 20:
Top -> 20 -> 10 -> None

Push 30:
Top -> 30 -> 20 -> 10 -> None

Pop:
30 is removed.

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Is Empty: O(1)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand how a Stack can be implemented using a Linked List.
- Connect Linked List concepts with Stack operations.
- Understand LIFO behavior.
- Practice pointer manipulation.
"""


class Node:
    """
    Represents a node in the linked list.
    """

    def __init__(self, data: int):
        self.data = data
        self.next = None


class Stack:
    """
    Represents a Stack implemented using a Singly Linked List.
    """

    def __init__(self):
        self.top = None

    def push(self, data: int) -> None:
        """
        Adds an element to the top of the stack.

        Args:
            data (int): Value to be inserted.
        """
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

    def pop(self) -> int | None:
        """
        Removes and returns the top element.

        Returns:
            int | None: Removed element, or None if the stack is empty.
        """
        if self.is_empty():
            print("Stack Underflow: Stack is empty.")
            return None

        removed_value = self.top.data
        self.top = self.top.next

        return removed_value

    def peek(self) -> int | None:
        """
        Returns the top element without removing it.

        Returns:
            int | None: Top element, or None if the stack is empty.
        """
        if self.is_empty():
            print("Stack is empty.")
            return None

        return self.top.data

    def is_empty(self) -> bool:
        """
        Checks whether the stack is empty.

        Returns:
            bool: True if empty, otherwise False.
        """
        return self.top is None

    def display(self) -> None:
        """
        Displays the stack from top to bottom.
        """
        if self.is_empty():
            print("Stack is empty.")
            return

        current = self.top

        print("Top")

        while current is not None:
            print(current.data)
            current = current.next

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
# • The top of the stack is represented by the head node.
# • Push and Pop operations are performed at the beginning of the linked list.
# • Both Push and Pop take O(1) time.
# • No Python list is used to store the stack elements.
# • Linked List implementation provides dynamic memory allocation.
