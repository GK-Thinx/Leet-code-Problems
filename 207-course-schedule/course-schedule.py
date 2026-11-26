from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indeg = [0]*numCourses
        g = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            g[b].append(a)
            indeg[a]+=1
        q=deque([i for i in range(numCourses) if indeg[i]==0])
        cnt=0
        while q:
            u=q.popleft()
            cnt+=1
            for v in g[u]:
                indeg[v]-=1
                if indeg[v]==0:
                    q.append(v)
        return cnt==numCourses