"""
Program: Merge Two Sorted Linked Lists

Description:
This program merges two sorted Singly Linked Lists into
one sorted linked list.

Instead of creating new nodes, the algorithm reuses the
existing nodes by updating their next pointers.

Example:

List 1:
10 -> 30 -> 50 -> None

List 2:
20 -> 40 -> 60 -> None

Merged List:
10 -> 20 -> 30 -> 40 -> 50 -> 60 -> None

Algorithm:
1. Create a dummy node.
2. Compare the current nodes of both lists.
3. Attach the smaller node to the merged list.
4. Move the corresponding pointer forward.
5. Attach the remaining nodes after one list ends.

Time Complexity:
- O(n + m)

Space Complexity:
- O(1)

Learning Outcomes:
- Understand how to merge two sorted linked lists.
- Learn efficient pointer manipulation.
- Practice a classic interview problem.
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

    def display(self) -> None:
        """
        Displays the linked list.
        """
        if self.head is None:
            print("None")
            return

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    @staticmethod
    def merge_sorted_lists(
        first: Node | None,
        second: Node | None
    ) -> Node | None:
        """
        Merges two sorted linked lists.

        Args:
            first (Node | None): Head of first linked list.
            second (Node | None): Head of second linked list.

        Returns:
            Node | None: Head of merged linked list.
        """
        dummy = Node(0)
        tail = dummy

        while first is not None and second is not None:

            if first.data <= second.data:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next

            tail = tail.next

        if first is not None:
            tail.next = first
        else:
            tail.next = second

        return dummy.next


if __name__ == "__main__":

    first_list = LinkedList()
    second_list = LinkedList()

    for value in [10, 30, 50]:
        first_list.insert_at_end(value)

    for value in [20, 40, 60]:
        second_list.insert_at_end(value)

    print("First Linked List:")
    first_list.display()

    print("\nSecond Linked List:")
    second_list.display()

    merged = LinkedList()
    merged.head = LinkedList.merge_sorted_lists(
        first_list.head,
        second_list.head
    )

    print("\nMerged Linked List:")
    merged.display()


# Key Takeaways:
# • The merged list remains sorted.
# • Existing nodes are reused instead of creating new ones.
# • A dummy node simplifies pointer handling.
# • Time Complexity: O(n + m)
# • Space Complexity: O(1)
# • This is one of the most frequently asked linked list interview questions.
