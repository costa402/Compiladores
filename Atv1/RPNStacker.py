class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)


def rpn_calculator(expr):
    stack = Stack()
    operators = ["+", "-", "*", "/"]
    for token in expr.split():
        if token.isdigit():
            stack.push(int(token))
        elif token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.push(a + b)
            elif token == "-":
                stack.push(a - b)
            elif token == "*":
                stack.push(a * b)
            elif token == "/":
                stack.push(a / b)
        else:
            print("Erro: Unexpected token:", token)
            return None
    return stack.pop()


filename = "rpn_expression.txt"
with open(filename, "r") as f:
    expr = f.read().strip()
    result = rpn_calculator(expr)
    print("Result:", result)