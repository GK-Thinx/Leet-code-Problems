class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        max_len = max(map(len, wordDict)) if wordDict else 0
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return [""]
            res = []
            for j in range(i + 1, min(len(s), i + max_len) + 1):
                w = s[i:j]
                if w in word_set:
                    for tail in dfs(j):
                        if tail:
                            res.append(w + " " + tail)
                        else:
                            res.append(w)
            return res
        return dfs(0)