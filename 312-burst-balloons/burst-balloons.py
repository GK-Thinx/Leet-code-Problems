class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        arr = [1] + nums + [1]
        m = n + 2
        dp = [[0] * m for _ in range(m)]
        for length in range(2, m):
            for left in range(0, m - length):
                right = left + length
                best = 0
                for k in range(left + 1, right):
                    val = dp[left][k] + dp[k][right] + arr[left] * arr[k] * arr[right]
                    if val > best:
                        best = val
                dp[left][right] = best
        return dp[0][m - 1]