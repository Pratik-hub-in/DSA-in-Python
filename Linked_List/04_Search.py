"""
Program: Search in a Singly Linked List

Description:
This program demonstrates how to search for a value
in a Singly Linked List.

The search operation traverses the linked list from the
head node until the required value is found or the end
of the list is reached.

Example:
Input Linked List:
10 -> 20 -> 30 -> 40

Search Value:
30

Output:
Value 30 found at position 3.

Time Complexity:
- Best Case: O(1)
- Average Case: O(n)
- Worst Case: O(n)

Space Complexity:
- O(1)

Learning Outcomes:
- Understand linear search in linked lists.
- Learn linked list traversal.
- Handle values that are not present.
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

        Args:
            data (int): Value to insert.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def search(self, value: int) -> int:
        """
        Searches for a value in the linked list.

        Args:
            value (int): Value to search.

        Returns:
            int: Position of the value (1-based indexing),
                 or -1 if not found.
        """
        current = self.head
        position = 1

        while current is not None:
            if current.data == value:
                return position

            current = current.next
            position += 1

        return -1

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

    print("Linked List:")
    linked_list.display()

    search_value = 30

    print(f"\nSearching for {search_value}...")

    position = linked_list.search(search_value)

    if position != -1:
        print(f"Value {search_value} found at position {position}.")
    else:
        print(f"Value {search_value} not found.")

    search_value = 50

    print(f"\nSearching for {search_value}...")

    position = linked_list.search(search_value)

    if position != -1:
        print(f"Value {search_value} found at position {position}.")
    else:
        print(f"Value {search_value} not found.")


# Key Takeaways:
# • Linked lists require linear search because random access is not possible.
# • Searching starts from the head node and continues until the value is found.
# • The worst-case time complexity is O(n).
# • Returning the node position is useful in many applications.
