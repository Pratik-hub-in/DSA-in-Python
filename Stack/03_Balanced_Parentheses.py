"""
Program: Balanced Parentheses

Description:
This program checks whether an expression contains
balanced parentheses using a Stack.

The expression can contain:
- Round brackets: ()
- Square brackets: []
- Curly brackets: {}

A valid expression must satisfy:
1. Every opening bracket has a matching closing bracket.
2. Brackets must close in the correct order.

Examples:

Valid:
{[()]}

Invalid:
{[(])}

Algorithm:
1. Create an empty stack.
2. Traverse the expression from left to right.
3. Push every opening bracket onto the stack.
4. For every closing bracket:
   - Check whether the stack is empty.
   - Check whether the top matches the closing bracket.
   - If not, the expression is invalid.
5. At the end, the stack must be empty.

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand a practical application of Stack.
- Learn bracket matching using LIFO.
- Practice handling nested expressions.
"""


class Stack:
    """
    Represents a Stack using a Python list.
    """

    def __init__(self):
        self.items = []

    def push(self, data: str) -> None:
        """
        Adds an element to the stack.
        """
        self.items.append(data)

    def pop(self) -> str | None:
        """
        Removes and returns the top element.

        Returns:
            str | None: Top element or None if empty.
        """
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self) -> str | None:
        """
        Returns the top element without removing it.

        Returns:
            str | None: Top element or None if empty.
        """
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self) -> bool:
        """
        Checks whether the stack is empty.
        """
        return len(self.items) == 0


def is_balanced(expression: str) -> bool:
    """
    Checks whether an expression has balanced parentheses.

    Args:
        expression (str): Expression containing brackets.

    Returns:
        bool: True if balanced, otherwise False.
    """
    stack = Stack()

    opening_brackets = {"(", "[", "{"}

    matching_brackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in expression:

        if character in opening_brackets:
            stack.push(character)

        elif character in matching_brackets:

            if stack.is_empty():
                return False

            if stack.pop() != matching_brackets[character]:
                return False

    return stack.is_empty()


if __name__ == "__main__":

    expressions = [
        "{[()]}",
        "((()))",
        "[{()}]",
        "{[(])}",
        "((())",
        "[(])"
    ]

    for expression in expressions:

        result = is_balanced(expression)

        if result:
            print(f"{expression} -> Balanced")
        else:
            print(f"{expression} -> Not Balanced")


# Key Takeaways:
# • Stack follows LIFO, which is perfect for matching brackets.
# • Opening brackets are pushed onto the stack.
# • Closing brackets are matched with the most recent opening bracket.
# • The expression is balanced only when the stack is empty at the end.
# • Time Complexity: O(n)
# • Space Complexity: O(n)
