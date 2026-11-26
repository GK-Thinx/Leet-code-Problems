import collections
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.od = collections.OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        val = self.od.pop(key)
        self.od[key] = val
        return val
    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.pop(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)