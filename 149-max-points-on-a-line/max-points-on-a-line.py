class Solution:
    def maxPoints(self, points):
        import math
        n = len(points)
        if n <= 2:
            return n
        ans = 0
        for i in range(n):
            slopes = {}
            dup = 0
            xi, yi = points[i]
            cur_max = 0
            for j in range(i + 1, n):
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi
                if dx == 0 and dy == 0:
                    dup += 1
                    continue
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                key = (dy, dx)
                slopes[key] = slopes.get(key, 0) + 1
                cur_max = max(cur_max, slopes[key])
            ans = max(ans, cur_max + dup + 1)
        return ans