from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        sorted_vals = sorted(set(arr))
        rank = {v: i + 1 for i, v in enumerate(sorted_vals)}
        return [rank[x] for x in arr]