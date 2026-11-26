class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0
        bucket_size = max(1, (mx - mn) // (n - 1))
        bucket_count = (mx - mn) // bucket_size + 1
        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        bucket_used = [False] * bucket_count
        for v in nums:
            idx = (v - mn) // bucket_size
            bucket_min[idx] = min(bucket_min[idx], v)
            bucket_max[idx] = max(bucket_max[idx], v)
            bucket_used[idx] = True
        prev_max = mn
        max_gap = 0
        for i in range(bucket_count):
            if not bucket_used[i]:
                continue
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        return max_gap