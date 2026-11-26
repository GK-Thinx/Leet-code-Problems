import random
class RandomizedSet:
    def __init__(self):
        self.arr=[]
        self.idx={}
    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val]=len(self.arr)
        self.arr.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        i=self.idx[val]
        last=self.arr[-1]
        self.arr[i]=last
        self.idx[last]=i
        self.arr.pop()
        del self.idx[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.arr)