class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        sieve = bytearray(b'\x01') * n
        sieve[0:2] = b'\x00\x00'
        limit = int(n ** 0.5) + 1
        for i in range(2, limit):
            if sieve[i]:
                step = i
                start = i * i
                sieve[start:n:step] = b'\x00' * ((n - start - 1) // step + 1)
        return sum(sieve)