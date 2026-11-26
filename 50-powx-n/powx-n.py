class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        negative = n < 0
        exp = -n if negative else n
        result = 1.0
        base = x
        while exp:
            if exp & 1:
                result *= base
            base *= base
            exp >>= 1
        return 1.0 / result if negative else result