import collections
import heapq
class Solution:
    def findItinerary(self, tickets):
        graph=collections.defaultdict(list)
        for a,b in tickets:
            heapq.heappush(graph[a],b)
        route=[]
        def visit(airport):
            while graph[airport]:
                nxt=heapq.heappop(graph[airport])
                visit(nxt)
            route.append(airport)
        visit("JFK")
        return route[::-1]