class Solution:
    def canJump(self, nums: list[int]) -> bool:
        far = 0
        for i, v in enumerate(nums):
            if i > far:
                return False
            far = max(far, i + v)
            if far >= len(nums) - 1:
                return True
        return True