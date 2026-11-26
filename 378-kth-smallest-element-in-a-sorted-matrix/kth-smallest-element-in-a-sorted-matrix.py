class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = 0
            i, j = n - 1, 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    cnt += i + 1
                    j += 1
                else:
                    i -= 1
            if cnt < k:
                lo = mid + 1
            else:
                hi = mid
        return lo