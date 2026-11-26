class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False
        size = valueDiff + 1
        bucket = {}
        for i, num in enumerate(nums):
            b = num // size
            if b in bucket:
                return True
            if b - 1 in bucket and abs(num - bucket[b - 1]) <= valueDiff:
                return True
            if b + 1 in bucket and abs(num - bucket[b + 1]) <= valueDiff:
                return True
            bucket[b] = num
            if i >= indexDiff:
                old = nums[i - indexDiff]
                old_b = old // size
                del bucket[old_b]
        return False