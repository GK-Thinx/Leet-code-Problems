from math import gcd
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        ans = 0
        for i in range(n):
            slopes = {}
            xi, yi = points[i]
            local_max = 0
            for j in range(i + 1, n):
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi
                if dx == 0:
                    key = (0, 0)
                elif dy == 0:
                    key = (0, 1)
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    key = (dy, dx)
                cnt = slopes.get(key, 0) + 1
                slopes[key] = cnt
                if cnt > local_max:
                    local_max = cnt
            ans = max(ans, local_max + 1)
        return ans