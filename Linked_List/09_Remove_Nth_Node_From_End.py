"""
Program: Remove Nth Node From End of a Singly Linked List

Description:
This program removes the Nth node from the end of a
Singly Linked List using the Two Pointer technique.

A dummy node is used to simplify handling edge cases,
such as removing the head node.

Example:

Input:
10 -> 20 -> 30 -> 40 -> 50 -> None

n = 2

Output:
10 -> 20 -> 30 -> 50 -> None

Algorithm:
1. Create a dummy node pointing to the head.
2. Move the fast pointer n + 1 steps ahead.
3. Move both slow and fast pointers together.
4. When fast reaches the end, slow will be just before
   the node to delete.
5. Update the next pointer to remove the target node.

Time Complexity:
- O(n)

Space Complexity:
- O(1)

Learning Outcomes:
- Understand the Two Pointer technique.
- Learn single-pass linked list traversal.
- Handle edge cases using a dummy node.
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

    def remove_nth_from_end(self, n: int) -> None:
        """
        Removes the Nth node from the end of the linked list.

        Args:
            n (int): Position from the end.
        """
        dummy = Node(0)
        dummy.next = self.head

        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            if fast is None:
                print("Invalid value of n.")
                return
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        if slow.next is not None:
            slow.next = slow.next.next

        self.head = dummy.next

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

    for value in [10, 20, 30, 40, 50]:
        linked_list.insert_at_end(value)

    print("Original Linked List:")
    linked_list.display()

    n = 2

    print(f"\nRemoving {n}nd node from the end...\n")

    linked_list.remove_nth_from_end(n)

    print("Updated Linked List:")
    linked_list.display()


# Key Takeaways:
# • A dummy node simplifies edge-case handling.
# • Fast pointer moves n + 1 steps ahead.
# • Slow pointer stops just before the target node.
# • The algorithm completes in a single traversal.
# • Time Complexity: O(n)
# • Space Complexity: O(1)
