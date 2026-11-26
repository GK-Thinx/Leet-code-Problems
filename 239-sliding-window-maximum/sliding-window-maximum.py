from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        if k == 1:
            return nums[:]
        dq = deque()
        res = []
        for i in range(n):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res