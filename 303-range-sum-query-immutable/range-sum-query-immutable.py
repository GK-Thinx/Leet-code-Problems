class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = [0]
        s = 0
        for v in nums:
            s += v
            self.prefix.append(s)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]