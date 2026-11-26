class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        cand1 = cand2 = None
        cnt1 = cnt2 = 0
        for num in nums:
            if cnt1 and num == cand1:
                cnt1 += 1
            elif cnt2 and num == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = num
                cnt1 = 1
            elif cnt2 == 0:
                cand2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = cnt2 = 0
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
        res = []
        n = len(nums)
        if cnt1 > n // 3:
            res.append(cand1)
        if cnt2 > n // 3:
            res.append(cand2)
        return res