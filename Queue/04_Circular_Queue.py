"""
Program: Circular Queue

Description:
A Circular Queue is a Queue in which the last position
is connected back to the first position.

It follows the FIFO (First In, First Out) principle.

In a normal fixed-size Queue, removing elements from the
front can create unused spaces.

Example:

Initial Queue:

[10] [20] [30] [40] [50]
 ↑                   ↑
front               rear

After removing 10 and 20:

[ ] [ ] [30] [40] [50]
         ↑          ↑
       front       rear

The first two positions are empty but cannot be reused
by a simple linear Queue.

Circular Queue solves this problem by wrapping the rear
around to the beginning.

Circular movement:

index = (index + 1) % capacity

Operations:
1. Enqueue
2. Dequeue
3. Front
4. Rear
5. Is Empty
6. Is Full
7. Display

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)
- Front: O(1)
- Rear: O(1)
- Is Empty: O(1)
- Is Full: O(1)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand Circular Queue.
- Learn how modulo operation creates circular movement.
- Understand front and rear pointer management.
- Learn how to efficiently reuse array space.
"""


class CircularQueue:
    """
    Represents a fixed-size Circular Queue.
    """

    def __init__(self, capacity: int):
        """
        Initializes the Circular Queue.

        Args:
            capacity (int): Maximum number of elements.
        """

        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.capacity = capacity
        self.queue = [None] * capacity

        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, data: int) -> bool:
        """
        Adds an element to the rear.

        Args:
            data (int): Value to be inserted.

        Returns:
            bool: True if inserted successfully,
                  False if Queue is full.
        """

        if self.is_full():
            print("Queue Overflow: Circular Queue is full.")
            return False

        self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = data
        self.size += 1

        return True

    def dequeue(self) -> int | None:
        """
        Removes and returns the front element.

        Returns:
            int | None: Removed element, or None if empty.
        """

        if self.is_empty():
            print("Queue Underflow: Circular Queue is empty.")
            return None

        value = self.queue[self.front]

        self.queue[self.front] = None

        self.front = (self.front + 1) % self.capacity

        self.size -= 1

        return value

    def peek_front(self) -> int | None:
        """
        Returns the front element without removing it.

        Returns:
            int | None: Front element, or None if empty.
        """

        if self.is_empty():
            print("Queue is empty.")
            return None

        return self.queue[self.front]

    def peek_rear(self) -> int | None:
        """
        Returns the rear element without removing it.

        Returns:
            int | None: Rear element, or None if empty.
        """

        if self.is_empty():
            print("Queue is empty.")
            return None

        return self.queue[self.rear]

    def is_empty(self) -> bool:
        """
        Checks whether the Queue is empty.

        Returns:
            bool: True if empty, otherwise False.
        """

        return self.size == 0

    def is_full(self) -> bool:
        """
        Checks whether the Queue is full.

        Returns:
            bool: True if full, otherwise False.
        """

        return self.size == self.capacity

    def display(self) -> None:
        """
        Displays elements from front to rear.
        """

        if self.is_empty():
            print("Queue is empty.")
            return

        print("Front ->", end=" ")

        index = self.front

        for _ in range(self.size):

            print(self.queue[index], end="")

            if _ < self.size - 1:
                print(" -> ", end="")

            index = (index + 1) % self.capacity

        print(" <- Rear")


if __name__ == "__main__":

    queue = CircularQueue(5)

    print("Enqueuing elements:")

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    queue.display()

    print("\nIs Queue Full?")
    print(queue.is_full())

    print("\nDequeued Element:")
    print(queue.dequeue())

    print("\nDequeued Element:")
    print(queue.dequeue())

    print("\nQueue After Dequeue:")
    queue.display()

    print("\nAdding elements after dequeue:")

    queue.enqueue(60)
    queue.enqueue(70)

    queue.display()

    print("\nFront Element:")
    print(queue.peek_front())

    print("\nRear Element:")
    print(queue.peek_rear())

    print("\nIs Queue Full?")
    print(queue.is_full())


# Key Takeaways:
# • Circular Queue reuses empty positions.
# • The modulo operator creates circular movement.
# • rear = (rear + 1) % capacity
# • front = (front + 1) % capacity
# • Enqueue and Dequeue both take O(1) time.
# • A size variable makes full and empty conditions easy to track.
