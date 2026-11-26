class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, cnt in freq.items():
            buckets[cnt].append(num)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res