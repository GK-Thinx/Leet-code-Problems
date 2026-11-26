class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
        while factor <= n:
            lower = n - (n // factor) * factor
            cur = (n // factor) % 10
            higher = n // (factor * 10)
            count += higher * factor
            if cur == 1:
                count += lower + 1
            elif cur > 1:
                count += factor
            factor *= 10
        return count