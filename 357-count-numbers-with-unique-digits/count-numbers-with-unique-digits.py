class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        total = 1
        for i in range(1, n + 1):
            cur = 9
            for j in range(1, i):
                cur *= 10 - j
            total += cur
        return total