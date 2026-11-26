class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = []
        def backtrack(i, path):
            if i == len(s):
                res.append(''.join(path))
                return
            if s[i].isdigit():
                path.append(s[i])
                backtrack(i + 1, path)
                path.pop()
            else:
                for c in (s[i].lower(), s[i].upper()):
                    path.append(c)
                    backtrack(i + 1, path)
                    path.pop()
        backtrack(0, [])
        return res