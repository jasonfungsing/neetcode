class Node:

    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.m = {}
        self.tm = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.m:
            n = self.tm[key]
            self.moveToTail(n)
            return self.m.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        n = Node(key, value)
        if key in self.m:
            self.m[key] = value
            og = self.tm[key]
            og.value = n.value
            self.tm[key] = og
            self.moveToTail(og)

        else:
            self.addToTail(n)
            self.m[key] = value
            self.tm[key] = n
            if len(self.m) > self.size:
                self.removeHead()

    def removeHead(self) -> None:
        n = self.head.next
        del self.m[n.key]
        del self.tm[n.key]
        left = self.head
        right = n.next

        left.next = right
        right.prev = left

    def moveToTail(self,n:Node) -> None:
        left = n.prev
        right = n.next
        left.next = right
        right.prev = left

        newLeft = self.tail.prev
        newRight = self.tail
        n.prev = newLeft
        n.next = newRight

        newLeft.next = n
        newRight.prev = n

    def addToTail(self,n:Node) -> None:
        left = self.tail.prev
        right = self.tail

        n.prev = left
        n.next = right

        left.next = n
        right.prev = n


            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)