from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        lengths = []
        for w in words:
            mask = 0
            for ch in set(w):
                mask |= 1 << (ord(ch) - 97)
            masks.append(mask)
            lengths.append(len(w))
        max_prod = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    prod = lengths[i] * lengths[j]
                    if prod > max_prod:
                        max_prod = prod
        return max_prod