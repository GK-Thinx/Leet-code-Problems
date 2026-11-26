import heapq
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        events.sort()
        res = []
        heap = [(0, float('inf'))]
        for x, neg_h, r in events:
            if neg_h:
                heapq.heappush(heap, (neg_h, r))
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)
            cur = -heap[0][0] if heap else 0
            if not res or res[-1][1] != cur:
                res.append([x, cur])
        return res