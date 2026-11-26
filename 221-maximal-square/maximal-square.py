class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n
        max_side = 0
        for i in range(m):
            prev = 0
            for j in range(n):
                temp = dp[j]
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[j] = 1
                    else:
                        dp[j] = 1 + min(dp[j], dp[j-1] if j > 0 else 0, prev)
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return max_side * max_side