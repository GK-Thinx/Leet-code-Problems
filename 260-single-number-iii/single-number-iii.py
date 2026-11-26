class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor_all = 0
        for n in nums:
            xor_all ^= n
        diff = xor_all & -xor_all
        a = 0
        b = 0
        for n in nums:
            if n & diff:
                a ^= n
            else:
                b ^= n
        return [a, b]