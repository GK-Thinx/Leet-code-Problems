class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = [0]*26
        for ch in s:
            cnt[ord(ch)-97] += 1
        res = []
        for ch in order:
            i = ord(ch)-97
            if cnt[i]:
                res.append(ch*cnt[i])
                cnt[i] = 0
        for i in range(26):
            if cnt[i]:
                res.append(chr(i+97)*cnt[i])
        return ''.join(res)