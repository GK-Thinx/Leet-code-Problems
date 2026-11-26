class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        import bisect
        dp = []
        for x in nums:
            i = bisect.bisect_left(dp, x)
            if i == len(dp):
                dp.append(x)
            else:
                dp[i] = x
        return len(dp)