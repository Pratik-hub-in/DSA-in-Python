"""
Program: Queue Using Deque

Description:
This program implements a Queue using Python's collections.deque.

A Queue follows the FIFO (First In, First Out) principle.

Example:

Enqueue:
10
20
30

Queue:
Front -> 10 -> 20 -> 30 <- Rear

Dequeue:
10 is removed.

Why deque?
------------
Using a Python list:
    enqueue  -> O(1)
    dequeue  -> O(n)

Using deque:
    enqueue  -> O(1)
    dequeue  -> O(1)

The deque data structure is therefore more suitable
for implementing a Queue.

Operations:
1. Enqueue
2. Dequeue
3. Front
4. Rear
5. Is Empty
6. Size
7. Display

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)
- Front: O(1)
- Rear: O(1)
- Is Empty: O(1)
- Size: O(1)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand the advantages of deque.
- Implement an efficient Queue.
- Compare list-based and deque-based Queues.
- Understand FIFO operations.
"""

from collections import deque


class Queue:
    """
    Represents a Queue using collections.deque.
    """

    def __init__(self):
        self.items = deque()

    def enqueue(self, data: int) -> None:
        """
        Adds an element to the rear of the Queue.

        Args:
            data (int): Value to be inserted.
        """
        self.items.append(data)

    def dequeue(self) -> int | None:
        """
        Removes and returns the front element.

        Returns:
            int | None: Removed element, or None if empty.
        """
        if self.is_empty():
            print("Queue Underflow: Queue is empty.")
            return None

        return self.items.popleft()

    def front(self) -> int | None:
        """
        Returns the front element without removing it.

        Returns:
            int | None: Front element, or None if empty.
        """
        if self.is_empty():
            print("Queue is empty.")
            return None

        return self.items[0]

    def rear(self) -> int | None:
        """
        Returns the rear element without removing it.

        Returns:
            int | None: Rear element, or None if empty.
        """
        if self.is_empty():
            print("Queue is empty.")
            return None

        return self.items[-1]

    def is_empty(self) -> bool:
        """
        Checks whether the Queue is empty.

        Returns:
            bool: True if empty, otherwise False.
        """
        return len(self.items) == 0

    def size(self) -> int:
        """
        Returns the number of elements in the Queue.

        Returns:
            int: Number of elements.
        """
        return len(self.items)

    def display(self) -> None:
        """
        Displays the Queue from front to rear.
        """
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Front ->", end=" ")

        for item in self.items:
            print(item, end=" -> ")

        print("Rear")


if __name__ == "__main__":

    queue = Queue()

    print("Enqueuing elements:")

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    queue.display()

    print("\nFront Element:")
    print(queue.front())

    print("\nRear Element:")
    print(queue.rear())

    print("\nQueue Size:")
    print(queue.size())

    print("\nDequeued Element:")
    print(queue.dequeue())

    print("\nQueue After Dequeue:")
    queue.display()

    print("\nIs Queue Empty?")
    print(queue.is_empty())


# Key Takeaways:
# • deque provides efficient insertion and removal from both ends.
# • append() adds an element to the rear in O(1).
# • popleft() removes an element from the front in O(1).
# • deque is preferred over list for a basic Queue implementation.
# • Queue follows the FIFO principle.
