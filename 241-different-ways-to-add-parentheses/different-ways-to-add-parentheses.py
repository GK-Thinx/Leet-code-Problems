class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}
        def compute(expr):
            if expr in memo:
                return memo[expr]
            res = []
            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    for a in left:
                        for b in right:
                            if ch == '+':
                                res.append(a + b)
                            elif ch == '-':
                                res.append(a - b)
                            else:
                                res.append(a * b)
            if not res:
                res.append(int(expr))
            memo[expr] = res
            return res
        return compute(expression)