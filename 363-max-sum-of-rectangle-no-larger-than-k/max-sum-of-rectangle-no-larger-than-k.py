from bisect import bisect_left, insort
class Solution:
    def maxSumSubmatrix(self, matrix, k):
        rows, cols = len(matrix), len(matrix[0])
        if rows > cols:
            matrix = [list(row) for row in zip(*matrix)]
            rows, cols = cols, rows
        max_sum = -10**9
        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                for c in range(cols):
                    col_sums[c] += matrix[bottom][c]
                prefix = [0]
                cur = 0
                for s in col_sums:
                    cur += s
                    idx = bisect_left(prefix, cur - k)
                    if idx < len(prefix):
                        max_sum = max(max_sum, cur - prefix[idx])
                    insort(prefix, cur)
        return max_sum