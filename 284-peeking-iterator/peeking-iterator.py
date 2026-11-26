class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self._has = self.it.hasNext()
        self._next = self.it.next() if self._has else None
    def peek(self):
        return self._next
    def next(self):
        cur = self._next
        self._has = self.it.hasNext()
        self._next = self.it.next() if self._has else None
        return cur
    def hasNext(self):
        return self._has