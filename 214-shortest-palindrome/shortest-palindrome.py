class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        rev = s[::-1]
        t = s + "#" + rev
        lps = [0] * len(t)
        for i in range(1, len(t)):
            j = lps[i - 1]
            while j > 0 and t[i] != t[j]:
                j = lps[j - 1]
            if t[i] == t[j]:
                j += 1
            lps[i] = j
        add = rev[:len(s) - lps[-1]]
        return add + s