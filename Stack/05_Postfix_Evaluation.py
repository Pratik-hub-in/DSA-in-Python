"""
Program: Postfix Expression Evaluation

Description:
This program evaluates a postfix expression using a Stack.

In postfix notation, operators are written after their operands.

Example:

Infix:
2 + 3 * 4

Postfix:
2 3 4 * +

Evaluation:
3 * 4 = 12
2 + 12 = 14

Result:
14

Supported Operators:
+  Addition
-  Subtraction
*  Multiplication
/  Division
%  Modulus
^  Exponentiation

Algorithm:
1. Traverse the postfix expression from left to right.
2. If the token is a number, push it onto the stack.
3. If the token is an operator:
   - Pop the second operand.
   - Pop the first operand.
   - Apply the operator.
   - Push the result back onto the stack.
4. The final element in the stack is the result.

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Understand postfix expression evaluation.
- Learn how Stack is used for arithmetic expressions.
- Practice operator processing and operand ordering.
"""


class Stack:
    """
    Represents a Stack using a Python list.
    """

    def __init__(self):
        self.items = []

    def push(self, data: float) -> None:
        """
        Adds an element to the stack.
        """
        self.items.append(data)

    def pop(self) -> float | None:
        """
        Removes and returns the top element.

        Returns:
            float | None: Top element or None if empty.
        """
        if self.is_empty():
            return None

        return self.items.pop()

    def is_empty(self) -> bool:
        """
        Checks whether the stack is empty.

        Returns:
            bool: True if empty, otherwise False.
        """
        return len(self.items) == 0


def apply_operator(operator: str, first: float, second: float) -> float:
    """
    Applies an arithmetic operator.

    Args:
        operator (str): Arithmetic operator.
        first (float): First operand.
        second (float): Second operand.

    Returns:
        float: Result of the operation.
    """
    if operator == "+":
        return first + second

    if operator == "-":
        return first - second

    if operator == "*":
        return first * second

    if operator == "/":
        return first / second

    if operator == "%":
        return first % second

    if operator == "^":
        return first ** second

    raise ValueError(f"Unsupported operator: {operator}")


def evaluate_postfix(expression: str) -> float:
    """
    Evaluates a postfix expression.

    Args:
        expression (str): Space-separated postfix expression.

    Returns:
        float: Evaluated result.
    """
    stack = Stack()

    tokens = expression.split()

    for token in tokens:

        if token.replace(".", "", 1).isdigit():
            stack.push(float(token))

        elif token in "+-*/%^":

            second = stack.pop()
            first = stack.pop()

            if first is None or second is None:
                raise ValueError("Invalid postfix expression.")

            result = apply_operator(token, first, second)

            stack.push(result)

        else:
            raise ValueError(f"Invalid token: {token}")

    if len(stack.items) != 1:
        raise ValueError("Invalid postfix expression.")

    result = stack.pop()

    if result is None:
        raise ValueError("Invalid postfix expression.")

    return result


if __name__ == "__main__":

    expressions = [
        "2 3 4 * +",
        "10 5 2 * +",
        "20 4 / 3 +",
        "5 1 2 + 4 * + 3 -",
        "2 3 ^"
    ]

    for expression in expressions:

        result = evaluate_postfix(expression)

        if result.is_integer():
            result = int(result)

        print(f"Postfix: {expression}")
        print(f"Result:  {result}")
        print()
