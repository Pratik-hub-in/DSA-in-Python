"""
Program: Deletion in a Singly Linked List

Description:
This program demonstrates different deletion operations
in a Singly Linked List.

Operations:
1. Delete from the beginning.
2. Delete from the end.
3. Delete a node by value.

Example:
Initial List:
10 -> 20 -> 30 -> 40

After delete_from_beginning():
20 -> 30 -> 40

After delete_from_end():
20 -> 30

After delete_by_value(20):
30

Algorithm:
1. Update the head for deletion at the beginning.
2. Traverse to the second-last node for deletion at the end.
3. Search for the target value and update pointers.

Time Complexity:
- Delete from Beginning : O(1)
- Delete from End       : O(n)
- Delete by Value       : O(n)

Space Complexity:
- O(1)

Learning Outcomes:
- Learn deletion operations in linked lists.
- Understand pointer manipulation.
- Handle edge cases such as empty and single-node lists.
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

    def delete_from_beginning(self) -> None:
        """
        Deletes the first node.
        """
        if self.head is None:
            print("Linked List is empty.")
            return

        self.head = self.head.next

    def delete_from_end(self) -> None:
        """
        Deletes the last node.
        """
        if self.head is None:
            print("Linked List is empty.")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        current.next = None

    def delete_by_value(self, value: int) -> None:
        """
        Deletes the first occurrence of the given value.

        Args:
            value (int): Value to delete.
        """
        if self.head is None:
            print("Linked List is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.data == value:
                previous.next = current.next
                return

            previous = current
            current = current.next

        print(f"{value} not found in the linked list.")

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

    print("Initial Linked List:")
    linked_list.display()

    linked_list.delete_from_beginning()

    print("\nAfter Deleting from Beginning:")
    linked_list.display()

    linked_list.delete_from_end()

    print("\nAfter Deleting from End:")
    linked_list.display()

    linked_list.delete_by_value(20)

    print("\nAfter Deleting Value 20:")
    linked_list.display()


# Key Takeaways:
# • Deleting the first node is an O(1) operation.
# • Deleting the last node requires traversal.
# • Always handle empty and single-node linked lists.
# • Update pointers carefully to avoid losing nodes.
