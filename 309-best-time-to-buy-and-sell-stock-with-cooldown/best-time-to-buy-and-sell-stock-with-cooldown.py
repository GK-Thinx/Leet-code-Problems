class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        hold = -prices[0]
        sold = 0
        rest = 0
        for p in prices[1:]:
            new_hold = max(hold, rest - p)
            new_sold = hold + p
            new_rest = max(rest, sold)
            hold, sold, rest = new_hold, new_sold, new_rest
        return max(sold, rest)