class Node:
    def __init__(self, prev, val, next):
        self.prev = prev
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node(None, -1 , None)
        self.tail = Node(self.head, -1, None)
        self.head.next = self.tail
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        n = self.head.next
        while index > 0:
            n = n.next
            index = index - 1
        return n.val

    def addAtHead(self, val: int) -> None:
        newhead = Node(self.head, val, self.head.next)
        self.head.next.prev = newhead
        self.head.next = newhead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newtail = Node(self.tail.prev, val, self.tail)
        self.tail.prev.next = newtail
        self.tail.prev = newtail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        p = self.head
        n = self.head.next
        while index > 0:
            p = n
            n = n.next
            index = index - 1
        newnode = Node(p, val, n)
        p.next = newnode
        n.prev = newnode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        p = self.head
        n = self.head.next
        while index > 0:
            p = n
            n = n.next
            index = index - 1
        nextn = n.next
        p.next = nextn
        nextn.prev = p
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)