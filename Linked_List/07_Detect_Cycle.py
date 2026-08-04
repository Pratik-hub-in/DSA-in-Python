"""
Program: Detect Cycle in a Singly Linked List

Description:
This program detects whether a Singly Linked List
contains a cycle using Floyd's Cycle Detection Algorithm
(Tortoise and Hare Algorithm).

A cycle exists when a node points back to a previously
visited node instead of pointing to None.

Algorithm:
1. Initialize two pointers:
   - slow = head
   - fast = head
2. Move slow by one node.
3. Move fast by two nodes.
4. If slow and fast meet, a cycle exists.
5. If fast reaches None, no cycle exists.

Example:

10 -> 20 -> 30 -> 40
      ^           |
      |___________|

Output:
Cycle Detected

Time Complexity:
- O(n)

Space Complexity:
- O(1)

Learning Outcomes:
- Understand Floyd's Cycle Detection Algorithm.
- Learn the Slow & Fast Pointer technique.
- Detect loops efficiently without extra memory.
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

    def create_cycle(self, position: int) -> None:
        """
        Creates a cycle for demonstration purposes.

        Args:
            position (int): 1-based position of the node
                            where the last node should point.
        """
        if self.head is None or position <= 0:
            return

        cycle_node = None
        current = self.head
        index = 1

        while current.next is not None:
            if index == position:
                cycle_node = current
            current = current.next
            index += 1

        if cycle_node is not None:
            current.next = cycle_node

    def detect_cycle(self) -> bool:
        """
        Detects whether the linked list contains a cycle.

        Returns:
            bool: True if a cycle exists, otherwise False.
        """
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def display(self) -> None:
        """
        Displays the linked list.

        Note:
        Do not call this method after creating a cycle,
        otherwise it will loop forever.
        """
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

    print("\nCycle Present Before Creation:")
    print(linked_list.detect_cycle())

    linked_list.create_cycle(2)

    print("\nCycle Present After Creation:")
    print(linked_list.detect_cycle())


# Key Takeaways:
# • Floyd's Algorithm uses two pointers moving at different speeds.
# • If a cycle exists, the pointers will eventually meet.
# • No extra data structure is required.
# • Time Complexity: O(n)
# • Space Complexity: O(1)
# • One of the most frequently asked Linked List interview problems.
