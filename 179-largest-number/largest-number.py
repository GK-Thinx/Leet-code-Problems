from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        strs = list(map(str, nums))
        def cmp(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0
        strs.sort(key=cmp_to_key(cmp))
        result = ''.join(strs)
        return '0' if result[0] == '0' else result