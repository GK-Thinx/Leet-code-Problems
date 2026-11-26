class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = 0
        for i in range(1, n + 1):
            s = str(i)
            if any(c in '347' for c in s):
                continue
            if any(c in '2569' for c in s):
                good += 1
        return good