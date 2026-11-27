class Solution:
    def canCross(self, stones):
        stone_set = set(stones)
        last = stones[-1]
        jumps = {0: {0}}
        for stone in stones:
            if stone not in jumps:
                continue
            for k in jumps[stone]:
                for step in (k - 1, k, k + 1):
                    if step > 0 and stone + step in stone_set:
                        jumps.setdefault(stone + step, set()).add(step)
        return bool(jumps.get(last))