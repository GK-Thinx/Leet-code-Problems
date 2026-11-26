class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif t == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif t == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif t == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack[0]