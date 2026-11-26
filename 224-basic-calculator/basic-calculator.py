class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if c.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                result += sign * num
                continue
            if c == '+':
                sign = 1
            elif c == '-':
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result
            i += 1
        return result