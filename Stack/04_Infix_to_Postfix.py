"""
Program: Infix to Postfix Conversion

Description:
This program converts an infix expression into a postfix
expression using a Stack.

Infix notation:
A + B * C

Postfix notation:
A B C * +

Operator precedence:
1. ^  -> Highest
2. *, /, %
3. +, -

The conversion uses a Stack to temporarily store operators.

Algorithm:
1. Traverse the expression from left to right.
2. If the character is an operand, add it to the output.
3. If the character is '(', push it onto the stack.
4. If the character is ')', pop operators until '(' is found.
5. If the character is an operator:
   - Pop operators with higher precedence.
   - Handle equal precedence according to associativity.
   - Push the current operator.
6. Pop all remaining operators from the stack.

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand infix and postfix notation.
- Learn operator precedence and associativity.
- Apply Stack to expression conversion.
- Understand a fundamental expression parsing technique.
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


def precedence(operator: str) -> int:
    """
    Returns the precedence of an operator.

    Args:
        operator (str): Arithmetic operator.

    Returns:
        int: Precedence value.
    """
    priorities = {
        "^": 3,
        "*": 2,
        "/": 2,
        "%": 2,
        "+": 1,
        "-": 1
    }

    return priorities.get(operator, 0)


def is_operator(character: str) -> bool:
    """
    Checks whether a character is an operator.

    Args:
        character (str): Character to check.

    Returns:
        bool: True if operator, otherwise False.
    """
    return character in "+-*/%^"


def infix_to_postfix(expression: str) -> str:
    """
    Converts an infix expression to postfix notation.

    Args:
        expression (str): Infix expression.

    Returns:
        str: Postfix expression.
    """
    stack = Stack()
    output = []

    for character in expression.replace(" ", ""):

        if character.isalnum():
            output.append(character)

        elif character == "(":
            stack.push(character)

        elif character == ")":

            while not stack.is_empty() and stack.peek() != "(":
                output.append(stack.pop())

            if not stack.is_empty():
                stack.pop()

        elif is_operator(character):

            while (
                not stack.is_empty()
                and stack.peek() != "("
                and precedence(stack.peek()) >= precedence(character)
            ):
                output.append(stack.pop())

            stack.push(character)

    while not stack.is_empty():
        output.append(stack.pop())

    return "".join(output)


if __name__ == "__main__":

    expressions = [
        "A+B*C",
        "(A+B)*C",
        "A+B*(C-D)",
        "A+B*C-D",
        "(A+B)*(C-D)"
    ]

    for expression in expressions:

        postfix = infix_to_postfix(expression)

        print(f"Infix:   {expression}")
        print(f"Postfix: {postfix}")
        print()
      
