import heapq
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        n1, n2 = len(nums1), len(nums2)
        heap = []
        for i in range(min(n1, k)):
            heap.append((nums1[i] + nums2[0], i, 0))
        heapq.heapify(heap)
        res = []
        while heap and len(res) < k:
            s, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res