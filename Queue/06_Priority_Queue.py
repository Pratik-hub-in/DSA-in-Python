"""
Program: Priority Queue Using Heap

Description:
A Priority Queue is a special type of Queue in which
each element is processed according to its priority.

In this implementation:
- Lower priority number means higher priority.
- Python's heapq module is used.
- The smallest priority value is removed first.

Example:

Insert:
Task A -> Priority 3
Task B -> Priority 1
Task C -> Priority 2

Removal order:

Task B -> Priority 1
Task C -> Priority 2
Task A -> Priority 3

Operations:
1. Insert
2. Remove highest-priority element
3. Peek highest-priority element
4. Check if empty
5. Get size
6. Display

Time Complexity:
- Insert: O(log n)
- Remove: O(log n)
- Peek: O(1)
- Is Empty: O(1)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand Priority Queue.
- Learn how heaps are used to implement Priority Queues.
- Understand min-heap behavior.
- Compare Priority Queue with normal Queue.
"""

import heapq


class PriorityQueue:
    """
    Implements a Min Priority Queue using heapq.
    """

    def __init__(self):
        self.heap = []

    def enqueue(self, data: str, priority: int) -> None:
        """
        Adds an element with a priority.

        Args:
            data (str): Element to insert.
            priority (int): Priority of the element.
                           Smaller value = higher priority.
        """

        heapq.heappush(self.heap, (priority, data))

    def dequeue(self) -> tuple[int, str] | None:
        """
        Removes and returns the highest-priority element.

        Returns:
            tuple[int, str] | None:
                (priority, data), or None if empty.
        """

        if self.is_empty():
            print("Priority Queue Underflow: Queue is empty.")
            return None

        return heapq.heappop(self.heap)

    def peek(self) -> tuple[int, str] | None:
        """
        Returns the highest-priority element without removing it.

        Returns:
            tuple[int, str] | None:
                (priority, data), or None if empty.
        """

        if self.is_empty():
            print("Priority Queue is empty.")
            return None

        return self.heap[0]

    def is_empty(self) -> bool:
        """
        Checks whether the Priority Queue is empty.

        Returns:
            bool: True if empty, otherwise False.
        """

        return len(self.heap) == 0

    def size(self) -> int:
        """
        Returns the number of elements.

        Returns:
            int: Number of elements.
        """

        return len(self.heap)

    def display(self) -> None:
        """
        Displays elements ordered by priority.

        Note:
        The internal heap list itself is NOT fully sorted,
        so a sorted copy is used only for display.
        """

        if self.is_empty():
            print("Priority Queue is empty.")
            return

        sorted_items = sorted(self.heap)

        print("Priority Queue:")

        for priority, data in sorted_items:
            print(f"Priority {priority} -> {data}")


if __name__ == "__main__":

    priority_queue = PriorityQueue()

    print("Adding elements:")

    priority_queue.enqueue("Task A", 3)
    priority_queue.enqueue("Task B", 1)
    priority_queue.enqueue("Task C", 2)
    priority_queue.enqueue("Task D", 1)

    priority_queue.display()

    print("\nHighest Priority Element:")
    print(priority_queue.peek())

    print("\nQueue Size:")
    print(priority_queue.size())

    print("\nRemoving elements by priority:")

    while not priority_queue.is_empty():
        priority, data = priority_queue.dequeue()
        print(f"Removed: {data} (Priority {priority})")

    print("\nIs Priority Queue Empty?")
    print(priority_queue.is_empty())


# Key Takeaways:
# • Priority Queue processes elements according to priority.
# • heapq implements a Min Heap by default.
# • Smaller priority value means higher priority here.
# • heappush() takes O(log n).
# • heappop() takes O(log n).
# • The smallest element is available at heap[0].
# • A heap's internal list is not completely sorted.
