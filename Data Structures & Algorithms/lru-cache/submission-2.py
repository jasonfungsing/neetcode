class Node:
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.m = {}
        self.cap = capacity
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.m:
            n = self.m.get(key)

            # remove it
            next = n.next
            n.prev.next = n.next
            next.prev = n.prev

            # reattach before tail
            prev = self.tail.prev
            prev.next = n
            self.tail.prev = n
            n.prev = prev
            n.next = self.tail

            return n.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.m:
            n = self.m.get(key)
            n.value = value
            
            n.prev.next = n.next

            n.next.prev = n.prev
            prev = self.tail.prev
            prev.next = n
            self.tail.prev = n
            n.prev = prev
            n.next = self.tail

        else:
            if len(self.m) >= self.cap:
                lru = self.head.next
                self.head.next = lru.next
                lru.next.prev = self.head
                
                del self.m[lru.key]

            n = Node(key, value)
            self.m[key] = n

            prev = self.tail.prev
            prev.next = n

            n.prev = prev
            n.next = self.tail
            self.tail.prev = n

