class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        seen_digit = False
        seen_dot = False
        seen_exp = False
        digit_after_exp = True
        for i, c in enumerate(s):
            if c in '+-':
                if i != 0 and s[i - 1] not in 'eE':
                    return False
            elif c.isdigit():
                seen_digit = True
                if seen_exp:
                    digit_after_exp = True
            elif c in 'eE':
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                digit_after_exp = False
            elif c == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            else:
                return False
        if seen_exp:
            return seen_digit and digit_after_exp
        return seen_digit