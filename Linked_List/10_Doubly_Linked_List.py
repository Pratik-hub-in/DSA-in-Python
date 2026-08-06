"""
Program: Doubly Linked List

Description:
A Doubly Linked List is a linear data structure where each node
contains:
1. Data
2. Reference to the previous node
3. Reference to the next node

Unlike a Singly Linked List, it allows traversal in both
forward and backward directions.

Example:

Forward:
10 <-> 20 <-> 30 <-> 40 <-> None

Backward:
40 <-> 30 <-> 20 <-> 10 <-> None

Algorithm:
1. Create a DoublyNode class.
2. Create a DoublyLinkedList class.
3. Insert nodes at the end.
4. Traverse forward.
5. Traverse backward.

Time Complexity:
- Insert at End: O(n)
- Forward Traversal: O(n)
- Backward Traversal: O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand the structure of a Doubly Linked List.
- Learn forward and backward traversal.
- Practice pointer manipulation using prev and next references.
"""


class DoublyNode:
    """
    Represents a node in a Doubly Linked List.
    """

    def __init__(self, data: int):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    Represents a Doubly Linked List.
    """

    def __init__(self):
        self.head = None

    def insert_at_end(self, data: int) -> None:
        """
        Inserts a node at the end of the linked list.
        """
        new_node = DoublyNode(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def display_forward(self) -> None:
        """
        Displays the linked list from head to tail.
        """
        if self.head is None:
            print("Doubly Linked List is empty.")
            return

        current = self.head

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")

    def display_backward(self) -> None:
        """
        Displays the linked list from tail to head.
        """
        if self.head is None:
            print("Doubly Linked List is empty.")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")


if __name__ == "__main__":

    doubly_linked_list = DoublyLinkedList()

    for value in [10, 20, 30, 40]:
        doubly_linked_list.insert_at_end(value)

    print("Forward Traversal:")
    doubly_linked_list.display_forward()

    print("\nBackward Traversal:")
    doubly_linked_list.display_backward()


# Key Takeaways:
# • Each node stores both previous and next references.
# • Traversal is possible in both directions.
# • Deletion is generally easier than in a Singly Linked List.
# • Doubly Linked Lists require extra memory for the prev pointer.
# • Widely used in browser history, undo/redo functionality, and LRU cache implementations.
