class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        pref = [0]
        s = 0
        for v in nums:
            s += v
            pref.append(s)
        def sort(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            cnt = sort(lo, mid) + sort(mid, hi)
            j = k = mid
            for i in range(lo, mid):
                while k < hi and pref[k] - pref[i] < lower:
                    k += 1
                while j < hi and pref[j] - pref[i] <= upper:
                    j += 1
                cnt += j - k
            l, r = lo, mid
            temp = []
            while l < mid and r < hi:
                if pref[l] <= pref[r]:
                    temp.append(pref[l])
                    l += 1
                else:
                    temp.append(pref[r])
                    r += 1
            while l < mid:
                temp.append(pref[l])
                l += 1
            while r < hi:
                temp.append(pref[r])
                r += 1
            pref[lo:hi] = temp
            return cnt
        return sort(0, len(pref))