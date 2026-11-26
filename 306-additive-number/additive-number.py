class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break
            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break
                a, b = num[:i], num[i:j]
                pos = j
                while pos < n:
                    s = str(int(a) + int(b))
                    if not num.startswith(s, pos):
                        break
                    pos += len(s)
                    a, b = b, s
                if pos == n and pos > j:
                    return True
        return False