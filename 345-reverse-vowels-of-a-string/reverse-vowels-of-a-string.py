class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        lst = list(s)
        i, j = 0, len(lst) - 1
        while i < j:
            while i < j and lst[i] not in vowels:
                i += 1
            while i < j and lst[j] not in vowels:
                j -= 1
            if i < j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
        return ''.join(lst)