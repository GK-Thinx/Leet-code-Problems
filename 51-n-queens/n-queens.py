class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [0] * n
        def backtrack(r, cols, d1, d2):
            if r == n:
                res.append(['.' * c + 'Q' + '.' * (n - c - 1) for c in board])
                return
            avail = (~(cols | d1 | d2)) & ((1 << n) - 1)
            while avail:
                p = avail & -avail
                c = (p - 1).bit_length()
                board[r] = c
                backtrack(r + 1, cols | p, (d1 | p) << 1, (d2 | p) >> 1)
                avail ^= p
        backtrack(0, 0, 0, 0)
        return res