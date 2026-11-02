class MinStack:

    def __init__(self):
        self.arr = []
        self.marr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.marr:
            self.marr.append(min(self.marr[-1],val))
        else:
            self.marr.append(val)
        

    def pop(self) -> None:
        self.arr.pop()
        self.marr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.marr[-1]
        
        
