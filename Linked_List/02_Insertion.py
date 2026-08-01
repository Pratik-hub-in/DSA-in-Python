"""
Program: Insertion in a Singly Linked List

Description:
This program demonstrates different insertion operations
in a Singly Linked List.

Operations:
1. Insert at the beginning.
2. Insert at the end.
3. Insert at a specific position.

Example:
Initial List:
10 -> 20 -> 30

After insert_at_beginning(5):
5 -> 10 -> 20 -> 30

After insert_at_end(40):
5 -> 10 -> 20 -> 30 -> 40

After insert_at_position(25, 4):
5 -> 10 -> 20 -> 25 -> 30 -> 40

Algorithm:
1. Create a new node.
2. Update node references based on the insertion position.
3. Display the updated linked list.

Time Complexity:
- Insert at Beginning : O(1)
- Insert at End       : O(n)
- Insert at Position  : O(n)

Space Complexity:
- O(1)

Learning Outcomes:
- Learn different insertion operations.
- Understand pointer manipulation.
- Practice linked list traversal.
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

    def insert_at_beginning(self, data: int) -> None:
        """
        Inserts a node at the beginning.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: int) -> None:
        """
        Inserts a node at the end.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def insert_at_position(self, data: int, position: int) -> None:
        """
        Inserts a node at a given position (1-based indexing).

        Args:
            data (int): Value to insert.
            position (int): Position where the node should be inserted.
        """
        if position <= 0:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        current_position = 1

        while current is not None and current_position < position - 1:
            current = current.next
            current_position += 1

        if current is None:
            print("Position out of range.")
            return

        new_node.next = current.next
        current.next = new_node

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

    print("Initial Linked List:")
    linked_list.display()

    linked_list.insert_at_beginning(5)

    print("\nAfter Inserting at Beginning:")
    linked_list.display()

    linked_list.insert_at_end(40)

    print("\nAfter Inserting at End:")
    linked_list.display()

    linked_list.insert_at_position(25, 4)

    print("\nAfter Inserting at Position 4:")
    linked_list.display()


# Key Takeaways:
# • Insertion at the beginning is the fastest operation.
# • Insertion at the end requires traversal.
# • Position-based insertion requires careful pointer updates.
# • Linked lists are efficient for insertions compared to arrays.
