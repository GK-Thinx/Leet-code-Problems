from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def valid(st):
            cnt = 0
            for ch in st:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    if cnt == 0:
                        return False
                    cnt -= 1
            return cnt == 0
        if valid(s):
            return [s]
        visited = {s}
        q = deque([s])
        res = []
        found = False
        while q:
            cur = q.popleft()
            if valid(cur):
                res.append(cur)
                found = True
            if found:
                continue
            for i in range(len(cur)):
                if cur[i] not in '()':
                    continue
                nxt = cur[:i] + cur[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        return res