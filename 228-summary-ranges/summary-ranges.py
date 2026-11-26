class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        if not nums:
            return res
        start = nums[0]
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                if start == end:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{end}")
                if i < len(nums):
                    start = nums[i]
        return res