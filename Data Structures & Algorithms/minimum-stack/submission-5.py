class MinStack:

    def __init__(self):
        self.arr = []
        self.marr = []
        
    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.marr or val <= self.marr[-1]:
            self.marr.append(val)
        
    def pop(self) -> None:
        if self.arr.pop() == self.marr[-1]:
            self.marr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.marr[-1]