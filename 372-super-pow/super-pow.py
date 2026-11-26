class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        mod = 1337
        a %= mod
        def mod_pow(x, n):
            res = 1
            while n:
                if n & 1:
                    res = res * x % mod
                x = x * x % mod
                n >>= 1
            return res
        result = 1
        for d in b:
            result = mod_pow(result, 10) * mod_pow(a, d) % mod
        return result