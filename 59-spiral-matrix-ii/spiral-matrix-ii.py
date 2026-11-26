class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        res = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                res[top][col] = num
                num += 1
            top += 1
            for row in range(top, bottom + 1):
                res[row][right] = num
                num += 1
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res[bottom][col] = num
                    num += 1
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res[row][left] = num
                    num += 1
                left += 1
        return res