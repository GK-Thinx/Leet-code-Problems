class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cnt_s = [0]*10
        cnt_g = [0]*10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cnt_s[int(s)] += 1
                cnt_g[int(g)] += 1
        cows = sum(min(cnt_s[i], cnt_g[i]) for i in range(10))
        return f"{bulls}A{cows}B"