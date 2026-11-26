class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        if n == 1:
            return 1
        k = len(primes)
        ugly = [1] * n
        idx = [0] * k
        next_mul = primes[:]
        for i in range(1, n):
            nxt = min(next_mul)
            ugly[i] = nxt
            for j in range(k):
                if next_mul[j] == nxt:
                    idx[j] += 1
                    next_mul[j] = ugly[idx[j]] * primes[j]
        return ugly[-1]