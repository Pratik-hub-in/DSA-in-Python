"""
Program: Circular Linked List

Description:
A Circular Linked List is a linked list in which the last node
points back to the first node instead of None.

Unlike a Singly Linked List, there is no NULL pointer at the end
of the list. Traversal continues in a circular manner.

Example:

        ┌────────────────────────────┐
        │                            │
        ▼                            │
10 -> 20 -> 30 -> 40 -> 50 ----------┘

Algorithm:
1. Create a Node class.
2. Create a CircularLinkedList class.
3. Insert nodes at the end.
4. Make the last node point to the head.
5. Traverse carefully to avoid infinite loops.

Time Complexity:
- Insert at End : O(n)
- Traversal      : O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand the Circular Linked List structure.
- Learn safe traversal techniques.
- Explore practical applications of circular data structures.
"""


class Node:
    """
    Represents a node in a Circular Linked List.
    """

    def __init__(self, data: int):
        self.data = data
        self.next = None


class CircularLinkedList:
    """
    Represents a Circular Linked List.
    """

    def __init__(self):
        self.head = None

    def insert_at_end(self, data: int) -> None:
        """
        Inserts a node at the end of the circular linked list.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def display(self) -> None:
        """
        Displays the circular linked list.
        """
        if self.head is None:
            print("Circular Linked List is empty.")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(Back to Head)")

    def count_nodes(self) -> int:
        """
        Counts the number of nodes.

        Returns:
            int: Total number of nodes.
        """
        if self.head is None:
            return 0

        count = 1
        current = self.head.next

        while current != self.head:
            count += 1
            current = current.next

        return count


if __name__ == "__main__":

    circular_list = CircularLinkedList()

    for value in [10, 20, 30, 40, 50]:
        circular_list.insert_at_end(value)

    print("Circular Linked List:")
    circular_list.display()

    print("\nNumber of Nodes:")
    print(circular_list.count_nodes())


# Key Takeaways:
# • The last node points back to the head node.
# • Traversal must stop when the head is reached again.
# • There is no None pointer at the end.
# • Circular Linked Lists are useful for Round Robin Scheduling.
# • They are also used in Circular Queues and Multiplayer Game Turn Management.
