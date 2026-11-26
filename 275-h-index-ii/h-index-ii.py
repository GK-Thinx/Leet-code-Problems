class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        lo, hi = 0, n - 1
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if citations[mid] >= n - mid:
                ans = n - mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans