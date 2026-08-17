"""
Program: Queue Using Linked List

Description:
This program implements a Queue using a Linked List.

A Queue follows the FIFO (First In, First Out) principle.

In this implementation:
- New elements are inserted at the rear.
- Elements are removed from the front.
- A linked list is used to store the elements.
- Two pointers are maintained:
    1. front
    2. rear

Example:

Front
  ↓
[10] -> [20] -> [30]
                    ↑
                   Rear

Dequeue:
10 is removed.

After Dequeue:

Front
  ↓
[20] -> [30]
          ↑
         Rear

Advantages:
- No fixed-size array is required.
- Enqueue is O(1).
- Dequeue is O(1).

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)
- Front: O(1)
- Rear: O(1)
- Is Empty: O(1)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand Queue implementation using Linked List.
- Learn how front and rear pointers work.
- Understand dynamic memory allocation.
- Connect Linked List concepts with Queue operations.
"""


class Node:
    """
    Represents a node in the linked list.
    """

    def __init__(self, data: int):
        self.data = data
        self.next = None


class Queue:
    """
    Represents a Queue using a Linked List.
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data: int) -> None:
        """
        Adds an element to the rear of the Queue.

        Args:
            data (int): Value to be inserted.
        """

        new_node = Node(data)

        # If Queue is empty
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return

        # Add node at the rear
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self) -> int | None:
        """
        Removes and returns the front element.

        Returns:
            int | None: Removed element, or None if empty.
        """

        if self.is_empty():
            print("Queue Underflow: Queue is empty.")
            return None

        removed_value = self.front.data

        self.front = self.front.next

        # If Queue becomes empty,
        # rear must also become None.
        if self.front is None:
            self.rear = None

        return removed_value

    def peek_front(self) -> int | None:
        """
        Returns the front element without removing it.

        Returns:
            int | None: Front element, or None if empty.
        """

        if self.is_empty():
            print("Queue is empty.")
            return None

        return self.front.data

    def peek_rear(self) -> int | None:
        """
        Returns the rear element without removing it.

        Returns:
            int | None: Rear element, or None if empty.
        """

        if self.is_empty():
            print("Queue is empty.")
            return None

        return self.rear.data

    def is_empty(self) -> bool:
        """
        Checks whether the Queue is empty.

        Returns:
            bool: True if empty, otherwise False.
        """

        return self.front is None

    def size(self) -> int:
        """
        Returns the number of elements in the Queue.

        Returns:
            int: Number of elements.
        """

        count = 0
        current = self.front

        while current is not None:
            count += 1
            current = current.next

        return count

    def display(self) -> None:
        """
        Displays the Queue from front to rear.
        """

        if self.is_empty():
            print("Queue is empty.")
            return

        current = self.front

        print("Front ->", end=" ")

        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" -> ", end="")

            current = current.next

        print(" <- Rear")


if __name__ == "__main__":

    queue = Queue()

    print("Enqueuing elements:")

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    queue.display()

    print("\nFront Element:")
    print(queue.peek_front())

    print("\nRear Element:")
    print(queue.peek_rear())

    print("\nQueue Size:")
    print(queue.size())

    print("\nDequeued Element:")
    print(queue.dequeue())

    print("\nQueue After Dequeue:")
    queue.display()

    print("\nDequeued Element:")
    print(queue.dequeue())

    print("\nQueue After Dequeue:")
    queue.display()

    print("\nIs Queue Empty?")
    print(queue.is_empty())


# Key Takeaways:
# • A Linked List can be used to implement a Queue.
# • front points to the first node.
# • rear points to the last node.
# • Enqueue adds a node at the rear.
# • Dequeue removes a node from the front.
# • Both Enqueue and Dequeue take O(1) time.
# • When the last element is removed, both front and rear become None.
