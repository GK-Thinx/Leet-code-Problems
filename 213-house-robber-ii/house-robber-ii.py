class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def helper(arr):
            a, b = 0, 0
            for v in arr:
                a, b = b, max(b, a + v)
            return b
        return max(helper(nums[:-1]), helper(nums[1:]))