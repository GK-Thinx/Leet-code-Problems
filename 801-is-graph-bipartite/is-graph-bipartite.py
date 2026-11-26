from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        for i in range(n):
            if colors[i] == -1:
                colors[i] = 0
                q = deque([i])
                while q:
                    u = q.popleft()
                    for v in graph[u]:
                        if colors[v] == -1:
                            colors[v] = 1 - colors[u]
                            q.append(v)
                        elif colors[v] == colors[u]:
                            return False
        return True