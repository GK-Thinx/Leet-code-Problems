class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    v = dp[i - c] + 1
                    if v < dp[i]:
                        dp[i] = v
        return dp[amount] if dp[amount] != amount + 1 else -1