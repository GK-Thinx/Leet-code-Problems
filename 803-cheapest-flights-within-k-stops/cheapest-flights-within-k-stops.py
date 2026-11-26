class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = 10**15
        dist = [INF] * n
        dist[src] = 0
        for _ in range(k + 1):
            ndist = dist[:]
            for u, v, w in flights:
                if dist[u] + w < ndist[v]:
                    ndist[v] = dist[u] + w
            dist = ndist
        return -1 if dist[dst] == INF else dist[dst]