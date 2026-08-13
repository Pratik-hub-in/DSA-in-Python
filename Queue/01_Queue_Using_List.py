"""
Program: Queue Using Python List

Description:
A Queue is a linear data structure that follows the
FIFO (First In, First Out) principle.

The element inserted first is the first element removed.

Example:

Enqueue:
10
20
30

Queue:
Front -> 10 -> 20 -> 30 <- Rear

Dequeue:
10 is removed.

Operations:
1. Enqueue
2. Dequeue
3. Front
4. Rear
5. Check if Empty
6. Display

Note:
Python lists can be used to implement a Queue, but removing
the first element using pop(0) takes O(n) time because all
remaining elements must be shifted.

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(n)
- Front: O(1)
- Rear: O(1)
- Is Empty: O(1)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand the Queue data structure.
- Learn the FIFO principle.
- Implement basic Queue operations.
- Understand the limitation of using a Python list for Queue.
"""


class Queue:
    """
    Represents a Queue using a Python list.
    """

    def __init__(self):
        self.items = []

    def enqueue(self, data: int) -> None:
        """
        Adds an element to the rear of the queue.

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

        return self.items.pop(0)

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
        Checks whether the queue is empty.

        Returns:
            bool: True if empty, otherwise False.
        """
        return len(self.items) == 0

    def display(self) -> None:
        """
        Displays the queue from front to rear.
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

    queue.display()

    print("\nFront Element:")
    print(queue.front())

    print("\nRear Element:")
    print(queue.rear())

    print("\nDequeued Element:")
    print(queue.dequeue())

    print("\nQueue After Dequeue:")
    queue.display()

    print("\nIs Queue Empty?")
    print(queue.is_empty())


# Key Takeaways:
# • Queue follows the FIFO principle.
# • Elements are inserted at the rear.
# • Elements are removed from the front.
# • Python list append() is O(1) amortized.
# • list.pop(0) is O(n) because elements must be shifted.
# • deque is preferred for efficient Queue implementation.
