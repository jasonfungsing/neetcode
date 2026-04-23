class Element:
    def __init__(self, val, min):
        self.val = val
        self.min = min

class MinStack:

    def __init__(self):
        self.arr = []
        self.min = None

    def push(self, val: int) -> None:
        self.arr.append(Element(val, self.min))
        if self.min is None:
            self.min = val
        elif val < self.min:
            self.min = val
        
    def pop(self) -> None:
        element = self.arr.pop()
        self.min = element.min

    def top(self) -> int:
        return self.arr[-1].val

    def getMin(self) -> int:
        return self.min
    