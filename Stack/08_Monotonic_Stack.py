"""
Program: Monotonic Stack

Description:
A Monotonic Stack is a stack whose elements are maintained
in either increasing or decreasing order.

Types:
1. Monotonic Increasing Stack
2. Monotonic Decreasing Stack

A Monotonic Stack is useful for problems involving:
- Next Greater Element
- Next Smaller Element
- Previous Greater Element
- Previous Smaller Element
- Daily Temperatures
- Largest Rectangle in Histogram

This program demonstrates:
1. Monotonic Increasing Stack
2. Monotonic Decreasing Stack
3. Next Greater Elements
4. Next Smaller Elements

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand the Monotonic Stack pattern.
- Learn increasing and decreasing stack techniques.
- Understand how elements are removed while maintaining order.
- Build a reusable pattern for advanced DSA problems.
"""


class MonotonicStack:
    """
    Provides operations using monotonic stack techniques.
    """

    @staticmethod
    def increasing_stack(numbers: list[int]) -> list[int]:
        """
        Creates a monotonic increasing stack.

        Smaller elements remain toward the bottom
        and larger elements toward the top.

        Args:
            numbers (list[int]): Input array.

        Returns:
            list[int]: Final increasing stack.
        """
        stack = []

        for number in numbers:

            while stack and stack[-1] > number:
                stack.pop()

            stack.append(number)

        return stack

    @staticmethod
    def decreasing_stack(numbers: list[int]) -> list[int]:
        """
        Creates a monotonic decreasing stack.

        Larger elements remain toward the bottom
        and smaller elements toward the top.

        Args:
            numbers (list[int]): Input array.

        Returns:
            list[int]: Final decreasing stack.
        """
        stack = []

        for number in numbers:

            while stack and stack[-1] < number:
                stack.pop()

            stack.append(number)

        return stack

    @staticmethod
    def next_greater(numbers: list[int]) -> list[int]:
        """
        Finds the next greater element for every element.

        Args:
            numbers (list[int]): Input array.

        Returns:
            list[int]: Next greater elements.
        """
        result = [-1] * len(numbers)
        stack = []

        for index in range(len(numbers) - 1, -1, -1):

            while stack and stack[-1] <= numbers[index]:
                stack.pop()

            if stack:
                result[index] = stack[-1]

            stack.append(numbers[index])

        return result

    @staticmethod
    def next_smaller(numbers: list[int]) -> list[int]:
        """
        Finds the next smaller element for every element.

        Args:
            numbers (list[int]): Input array.

        Returns:
            list[int]: Next smaller elements.
        """
        result = [-1] * len(numbers)
        stack = []

        for index in range(len(numbers) - 1, -1, -1):

            while stack and stack[-1] >= numbers[index]:
                stack.pop()

            if stack:
                result[index] = stack[-1]

            stack.append(numbers[index])

        return result


if __name__ == "__main__":

    numbers = [4, 2, 5, 1, 3]

    print("Input:")
    print(numbers)

    print("\nMonotonic Increasing Stack:")
    print(MonotonicStack.increasing_stack(numbers))

    print("\nMonotonic Decreasing Stack:")
    print(MonotonicStack.decreasing_stack(numbers))

    print("\nNext Greater Elements:")
    print(MonotonicStack.next_greater(numbers))

    print("\nNext Smaller Elements:")
    print(MonotonicStack.next_smaller(numbers))


# Key Takeaways:
# • A Monotonic Stack maintains elements in a specific order.
# • Increasing stacks are useful for finding smaller elements.
# • Decreasing stacks are useful for finding greater elements.
# • Elements are removed when they violate the required order.
# • Each element is pushed and popped at most once in typical applications.
# • Most Monotonic Stack algorithms run in O(n) time.
