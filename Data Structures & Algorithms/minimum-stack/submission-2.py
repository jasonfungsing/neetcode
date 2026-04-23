class Element:
    def __init__(self, val, min):
        self.val = val
        self.min = min

class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        new_min = min(val, self.arr[-1].min if self.arr else val)
        self.arr.append(Element(val, new_min))
        
    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1].val

    def getMin(self) -> int:
        return self.arr[-1].min
    