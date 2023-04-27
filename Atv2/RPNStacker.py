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


def scan_tokens(expr):
    tokens = []
    operators = ["+", "-", "*", "/"]
    for token in expr.split():
        if token.isdigit():
            tokens.append(("NUM", int(token)))
        elif token in operators:
            if token == "+":
                tokens.append(("PLUS", token))
            if token == "-":
                tokens.append(("MINUS", token))
            if token == "*":
                tokens.append(("STAR", token))
            if token == "/":
                tokens.append(("SLASH", token))
        else:
            print("Erro: Unexpected token:", token)
            return None
    return tokens

def show_tokens(tokens):
    for token in tokens:
        print("Token [type=" + token[0] + ", lexeme=" + str(token[1]) + "]")
    return None

def evaluate(tokens):
    stack = Stack()
    for token in tokens:
        if token[0] == "NUM":
            stack.push(token[1])
        else:
            b = stack.pop()
            a = stack.pop()
            if token[1] == "+":
                stack.push(a + b)
            elif token[1] == "-":
                stack.push(a - b)
            elif token[1] == "*":
                stack.push(a * b)
            elif token[1] == "/":
                stack.push(a / b)
    return stack.pop()


filename = "rpn_expression.txt"
with open(filename, "r") as f:
    expr = f.read().strip()
    tokens = scan_tokens(expr)
    if tokens is not None:
        print("Tokens percived:\n")
        show_tokens(tokens)
        result = evaluate(tokens)
        print("\nResult:", result)
