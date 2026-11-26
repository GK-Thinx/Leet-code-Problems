class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        lo, hi = 0.0, 1.0
        ans_num, ans_den = 0, 1
        for _ in range(40):
            mid = (lo + hi) / 2
            count = 0
            i = 0
            best_num, best_den = 0, 1
            for j in range(1, n):
                while i < j and arr[i] / arr[j] <= mid:
                    i += 1
                count += i
                if i:
                    if best_num * arr[j] < arr[i - 1] * best_den:
                        best_num, best_den = arr[i - 1], arr[j]
            if count < k:
                lo = mid
            else:
                ans_num, ans_den = best_num, best_den
                hi = mid
        return [ans_num, ans_den]