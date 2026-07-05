class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        num=x
        if num<0:
            return False
        while num!=0:
            rev = rev*10 + num %10
            num = num // 10
        return rev == x

        