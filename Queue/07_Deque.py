"""
Program: Double-Ended Queue (Deque)

Description:
A Deque (Double-Ended Queue) is a linear data structure
where elements can be inserted and removed from both
the front and the rear.

Example:

             insert_front()
                   ↓
Front -> [10] [20] [30] <- Rear
           ↑             ↑
      delete_front   delete_rear

Operations:
1. Insert at Front
2. Insert at Rear
3. Delete from Front
4. Delete from Rear
5. Get Front
6. Get Rear
7. Check if Empty
8. Get Size
9. Display

Python's collections.deque is used because it provides
efficient operations at both ends.

Time Complexity:
- Insert Front: O(1)
- Insert Rear: O(1)
- Delete Front: O(1)
- Delete Rear: O(1)
- Front: O(1)
- Rear: O(1)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand Double-Ended Queue.
- Learn insertion and deletion from both ends.
- Understand practical applications of Deque.
- Compare Queue and Deque.
"""

from collections import deque


class Deque:
    """
    Implements a Double-Ended Queue using collections.deque.
    """

    def __init__(self):
        self.items = deque()

    def insert_front(self, data: int) -> None:
        """
        Inserts an element at the front.
        """
        self.items.appendleft(data)

    def insert_rear(self, data: int) -> None:
        """
        Inserts an element at the rear.
        """
        self.items.append(data)

    def delete_front(self) -> int | None:
        """
        Removes and returns the front element.
        """
        if self.is_empty():
            print("Deque Underflow: Deque is empty.")
            return None

        return self.items.popleft()

    def delete_rear(self) -> int | None:
        """
        Removes and returns the rear element.
        """
        if self.is_empty():
            print("Deque Underflow: Deque is empty.")
            return None

        return self.items.pop()

    def get_front(self) -> int | None:
        """
        Returns the front element without removing it.
        """
        if self.is_empty():
            print("Deque is empty.")
            return None

        return self.items[0]

    def get_rear(self) -> int | None:
        """
        Returns the rear element without removing it.
        """
        if self.is_empty():
            print("Deque is empty.")
            return None

        return self.items[-1]

    def is_empty(self) -> bool:
        """
        Checks whether the Deque is empty.
        """
        return len(self.items) == 0

    def size(self) -> int:
        """
        Returns the number of elements.
        """
        return len(self.items)

    def display(self) -> None:
        """
        Displays elements from front to rear.
        """
        if self.is_empty():
            print("Deque is empty.")
            return

        print("Front ->", end=" ")

        for index, value in enumerate(self.items):

            print(value, end="")

            if index < len(self.items) - 1:
                print(" <-> ", end="")

        print(" <- Rear")


if __name__ == "__main__":

    deque_structure = Deque()

    print("Inserting elements at rear:")

    deque_structure.insert_rear(20)
    deque_structure.insert_rear(30)
    deque_structure.insert_rear(40)

    deque_structure.display()

    print("\nInserting element at front:")

    deque_structure.insert_front(10)

    deque_structure.display()

    print("\nFront Element:")
    print(deque_structure.get_front())

    print("\nRear Element:")
    print(deque_structure.get_rear())

    print("\nDeque Size:")
    print(deque_structure.size())

    print("\nDeleting from front:")
    print(deque_structure.delete_front())

    deque_structure.display()

    print("\nDeleting from rear:")
    print(deque_structure.delete_rear())

    deque_structure.display()

    print("\nIs Deque Empty?")
    print(deque_structure.is_empty())


# Key Takeaways:
# • Deque means Double-Ended Queue.
# • Insertion is possible at both ends.
# • Deletion is possible at both ends.
# • appendleft() inserts at the front.
# • append() inserts at the rear.
# • popleft() removes from the front.
# • pop() removes from the rear.
# • All four operations take O(1) time.
