class Solution:
    def maxNumber(self, nums1, nums2, k):
        def pick(nums, t):
            drop = len(nums) - t
            stack = []
            for d in nums:
                while drop and stack and stack[-1] < d:
                    stack.pop()
                    drop -= 1
                stack.append(d)
            return stack[:t]
        def merge(a, b):
            res = []
            i = j = 0
            while i < len(a) or j < len(b):
                if a[i:] > b[j:]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            return res
        m, n = len(nums1), len(nums2)
        best = [0] * k
        start = max(0, k - n)
        end = min(k, m)
        for i in range(start, end + 1):
            part1 = pick(nums1, i)
            part2 = pick(nums2, k - i)
            candidate = merge(part1, part2)
            if candidate > best:
                best = candidate
        return best