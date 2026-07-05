class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        result = 0
        for i in range(len(s)):
            currnt_val = roman_nums[s[i]]
            # Next value for NUmbers like 4 have 'IV' and 6 have 'VI'
            next_val = roman_nums[s[i+1]] if i+1 < len(s) else 0 
            if currnt_val < next_val:
                result -= currnt_val
            else:
                result += currnt_val
        return result

        