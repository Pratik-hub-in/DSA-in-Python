"""
Program: Singly Linked List

Description:
A Singly Linked List is a linear data structure where each node
contains two parts:
1. Data
2. Reference (pointer) to the next node

Unlike arrays, linked lists do not store elements in contiguous
memory locations. Each node points to the next node, forming a chain.

Example:
Input:
10 → 20 → 30 → 40

Output:
10 -> 20 -> 30 -> 40 -> None

Algorithm:
1. Create a Node class.
2. Create a LinkedList class.
3. Implement append() to add nodes.
4. Implement display() to print the list.

Time Complexity:
- Append: O(n)
- Display: O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand Node and Linked List concepts.
- Learn basic Object-Oriented Programming.
- Build a linked list from scratch.
"""


class Node:
    """
    Represents a single node in a linked list.
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

    def append(self, data: int) -> None:
        """
        Adds a new node at the end of the linked list.

        Args:
            data (int): Value to be inserted.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self) -> None:
        """
        Displays all nodes in the linked list.
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

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)

    print("Singly Linked List:")
    linked_list.display()


# Key Takeaways:
# • A linked list consists of nodes connected through pointers.
# • Each node stores data and a reference to the next node.
# • Linked lists allow dynamic memory allocation.
# • They are efficient for insertions and deletions compared to arrays.
