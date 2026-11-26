class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        n = len(nums)
        mid = sorted(nums)[n // 2]
        def idx(i):
            return (1 + 2 * i) % (n | 1)
        left, i, right = 0, 0, n - 1
        while i <= right:
            vi = idx(i)
            if nums[vi] > mid:
                vleft = idx(left)
                nums[vi], nums[vleft] = nums[vleft], nums[vi]
                left += 1
                i += 1
            elif nums[vi] < mid:
                vright = idx(right)
                nums[vi], nums[vright] = nums[vright], nums[vi]
                right -= 1
            else:
                i += 1