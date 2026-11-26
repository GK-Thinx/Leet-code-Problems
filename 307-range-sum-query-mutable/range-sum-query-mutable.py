class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)
        for i, v in enumerate(nums):
            j = i + 1
            while j <= self.n:
                self.bit[j] += v
                j += j & -j
    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i <= self.n:
            self.bit[i] += diff
            i += i & -i
    def sumRange(self, left, right):
        def prefix(i):
            s = 0
            while i > 0:
                s += self.bit[i]
                i -= i & -i
            return s
        return prefix(right + 1) - prefix(left)