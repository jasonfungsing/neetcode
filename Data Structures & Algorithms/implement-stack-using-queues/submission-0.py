class MyStack:
    q1 = None
    q2 = None
    cq = None


    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.cq = self.q1
        self.aq = self.q2
        

    def push(self, x: int) -> None:
        self.cq.append(x)

    def pop(self) -> int:
        while len(self.cq) > 1:
            cur = self.cq.pop(0)
            self.aq.append(cur)
        item = self.cq.pop(0)
        self.cq, self.aq = self.aq, self.cq
        return item

    def top(self) -> int:
        while len(self.cq) > 0:
            cur = self.cq.pop(0)
            self.aq.append(cur)

        self.cq, self.aq = self.aq, self.cq
        return cur

    def empty(self) -> bool:
        return len(self.cq) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()