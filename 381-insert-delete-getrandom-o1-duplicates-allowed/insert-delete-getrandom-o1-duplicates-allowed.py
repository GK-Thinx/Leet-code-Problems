import random
class RandomizedCollection:
    def __init__(self):
        self.nums=[]
        self.idx={}
    def insert(self, val: int) -> bool:
        present=val in self.idx and self.idx[val]
        self.nums.append(val)
        self.idx.setdefault(val,set()).add(len(self.nums)-1)
        return not present
    def remove(self, val: int) -> bool:
        if val not in self.idx or not self.idx[val]:
            return False
        remove_idx=self.idx[val].pop()
        last=self.nums[-1]
        if remove_idx!=len(self.nums)-1:
            self.nums[remove_idx]=last
            self.idx[last].remove(len(self.nums)-1)
            self.idx[last].add(remove_idx)
        self.nums.pop()
        if not self.idx[val]:
            del self.idx[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.nums)