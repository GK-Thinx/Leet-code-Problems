class Solution:
    def countSmaller(self, nums):
        vals = {v:i+1 for i,v in enumerate(sorted(set(nums)))}
        size = len(vals)
        bit = [0]*(size+1)
        def add(i):
            while i<=size:
                bit[i]+=1
                i+=i&-i
        def query(i):
            s=0
            while i>0:
                s+=bit[i]
                i-=i&-i
            return s
        res=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            idx=vals[nums[i]]
            res[i]=query(idx-1)
            add(idx)
        return res