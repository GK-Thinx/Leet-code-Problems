class Solution:
    def palindromePairs(self, words):
        idx = {w: i for i, w in enumerate(words)}
        res = set()
        for i, w in enumerate(words):
            n = len(w)
            for cut in range(n + 1):
                left, right = w[:cut], w[cut:]
                if left == left[::-1]:
                    rev = right[::-1]
                    j = idx.get(rev)
                    if j is not None and j != i:
                        res.add((j, i))
                if cut != n and right == right[::-1]:
                    rev = left[::-1]
                    j = idx.get(rev)
                    if j is not None and j != i:
                        res.add((i, j))
        return [list(p) for p in res]