class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.cap = capacity
        self.f = []

    def get(self, key: int) -> int:
        if key in self.m:
            self.f.remove(key)
            self.f.append(key)
            return self.m.get(key)
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m[key] = value
            self.f.remove(key)
            self.f.append(key)
        else:
            if len(self.m) >= self.cap:
                first_value = self.f.pop(0)
                del self.m[first_value]
            self.m[key] = value
            self.f.append(key)
        

        
        

        
