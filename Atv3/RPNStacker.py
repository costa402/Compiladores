import re


class Regex:
    def __init__(self):
        self.num_pattern = r"\d+"
        self.op_pattern = r"[+\-*/]"
        
    def scan_tokens(self, expr):
        tokens = []
        for token in expr.split():
            if re.match(self.num_pattern, token):
                tokens.append(("NUM", int(token)))
            elif re.match(self.op_pattern, token):
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


def show_tokens(tokens):
    for token in tokens:
        print("Token [type=" + token[0] + ", lexeme=" + str(token[1]) + "]")
    return None


regex = Regex()
filename = "rpn_expression.txt"
with open(filename, "r") as f:
    expr = f.read().strip()
    tokens = regex.scan_tokens(expr)
    if tokens is not None:
        stack = Stack()
        for token in tokens:
            if token[0] == "NUM":
                stack.push(token[1])
            else:
                b = stack.pop()
                a = stack.pop()
                if token[0] == "PLUS":
                    stack.push(a + b)
                elif token[0] == "MINUS":
                    stack.push(a - b)
                elif token[0] == "STAR":
                    stack.push(a * b)
                elif token[0] == "SLASH":
                    stack.push(a / b)
        result = stack.pop()
        print("Tokens percived:\n")
        show_tokens(tokens)
        print("\nResult:", result)
