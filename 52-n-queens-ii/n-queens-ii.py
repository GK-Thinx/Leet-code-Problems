class Solution:
    def totalNQueens(self, n: int) -> int:
        mask = (1 << n) - 1
        count = 0
        def backtrack(cols, diags, anti):
            nonlocal count
            if cols == mask:
                count += 1
                return
            avail = mask & ~(cols | diags | anti)
            while avail:
                p = avail & -avail
                avail -= p
                backtrack(cols | p, (diags | p) << 1, (anti | p) >> 1)
        backtrack(0, 0, 0)
        return count