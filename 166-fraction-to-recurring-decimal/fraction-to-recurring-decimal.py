class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        n, d = abs(numerator), abs(denominator)
        integer_part = n // d
        remainder = n % d
        if remainder == 0:
            return sign + str(integer_part)
        res = [sign + str(integer_part), '.']
        seen = {}
        while remainder:
            if remainder in seen:
                idx = seen[remainder]
                res.insert(idx + 2, '(')
                res.append(')')
                break
            seen[remainder] = len(res) - 2
            remainder *= 10
            digit = remainder // d
            res.append(str(digit))
            remainder %= d
        return ''.join(res)