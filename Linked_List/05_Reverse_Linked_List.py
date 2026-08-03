"""
Program: Reverse a Singly Linked List

Description:
This program demonstrates how to reverse a Singly Linked List
using the iterative approach.

In a linked list reversal, the direction of every link is
changed so that the last node becomes the first node.

Example:
Original List:
10 -> 20 -> 30 -> 40 -> 50 -> None

Reversed List:
50 -> 40 -> 30 -> 20 -> 10 -> None

Algorithm:
1. Initialize three pointers:
   - previous = None
   - current = head
   - next_node = None
2. Traverse the linked list.
3. Reverse the link of the current node.
4. Move all pointers one step ahead.
5. Update the head to the last processed node.

Time Complexity:
- O(n)

Space Complexity:
- O(1)

Learning Outcomes:
- Learn in-place linked list reversal.
- Understand pointer manipulation.
- Practice one of the most important interview problems.
"""


class Node:
    """
    Represents a node in the linked list.
    """

    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    """
    Represents a Singly Linked List.
    """

    def __init__(self):
        self.head = None

    def insert_at_end(self, data: int) -> None:
        """
        Inserts a node at the end of the linked list.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def reverse(self) -> None:
        """
        Reverses the linked list using the iterative approach.
        """
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def display(self) -> None:
        """
        Displays the linked list.
        """
        if self.head is None:
            print("Linked List is empty.")
            return

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


if __name__ == "__main__":

    linked_list = LinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)

    print("Original Linked List:")
    linked_list.display()

    linked_list.reverse()

    print("\nReversed Linked List:")
    linked_list.display()


# Key Takeaways:
# • Linked list reversal is performed by changing node pointers.
# • The iterative approach uses three pointers:
#   previous, current, and next_node.
# • No extra linked list is created.
# • This algorithm runs in O(n) time and O(1) space.
# • Reverse Linked List is one of the most frequently asked coding interview questions.
