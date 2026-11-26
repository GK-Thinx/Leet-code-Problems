class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res = []
        n = len(num)
        def dfs(i, expr, val, prev):
            if i == n:
                if val == target:
                    res.append(expr)
                return
            for j in range(i, n):
                if j > i and num[i] == '0':
                    break
                cur_str = num[i:j+1]
                cur = int(cur_str)
                if i == 0:
                    dfs(j+1, cur_str, cur, cur)
                else:
                    dfs(j+1, expr + '+' + cur_str, val + cur, cur)
                    dfs(j+1, expr + '-' + cur_str, val - cur, -cur)
                    dfs(j+1, expr + '*' + cur_str, val - prev + prev * cur, prev * cur)
        dfs(0, "", 0, 0)
        return res