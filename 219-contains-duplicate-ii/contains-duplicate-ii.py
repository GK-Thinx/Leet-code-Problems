class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        s=set()
        for i,num in enumerate(nums):
            if num in s:
                return True
            s.add(num)
            if i>=k:
                s.remove(nums[i-k])
        return False