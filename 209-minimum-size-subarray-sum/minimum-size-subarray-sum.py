class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        cur = 0
        res = len(nums) + 1
        for right, val in enumerate(nums):
            cur += val
            while cur >= target:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        return 0 if res == len(nums) + 1 else res