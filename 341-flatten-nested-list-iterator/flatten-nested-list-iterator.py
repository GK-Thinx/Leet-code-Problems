class NestedIterator:
    def __init__(self, nestedList):
        self.flat = []
        self._flatten(nestedList)
        self.idx = 0
    def _flatten(self, lst):
        for ni in lst:
            if ni.isInteger():
                self.flat.append(ni.getInteger())
            else:
                self._flatten(ni.getList())
    def next(self):
        val = self.flat[self.idx]
        self.idx += 1
        return val
    def hasNext(self):
        return self.idx < len(self.flat)