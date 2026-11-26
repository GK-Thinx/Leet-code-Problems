class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_current = max_global = nums[0]
        for x in nums[1:]:
            max_current = x if max_current < 0 else max_current + x
            if max_current > max_global:
                max_global = max_current
        return max_global