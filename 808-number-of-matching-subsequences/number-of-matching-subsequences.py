from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        buckets = defaultdict(list)
        for w in words:
            it = iter(w)
            first = next(it, None)
            if first is not None:
                buckets[first].append(it)
        count = 0
        for ch in s:
            old = buckets[ch]
            buckets[ch] = []
            for it in old:
                nxt = next(it, None)
                if nxt is None:
                    count += 1
                else:
                    buckets[nxt].append(it)
        return count