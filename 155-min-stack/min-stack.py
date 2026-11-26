class MinStack:
    def __init__(self):
        self.s = []
        self.m = []
    def push(self, value: int) -> None:
        self.s.append(value)
        if not self.m or value <= self.m[-1]:
            self.m.append(value)
        else:
            self.m.append(self.m[-1])
    def pop(self) -> None:
        self.s.pop()
        self.m.pop()
    def top(self) -> int:
        return self.s[-1]
    def getMin(self) -> int:
        return self.m[-1]