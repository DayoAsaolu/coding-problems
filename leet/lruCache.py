class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.item = {}
        self.uCache = {}
        self.Maxkey = -1
        self.Minkey = -1

    def get(self, key: int) -> int:
        if key in self.item:
            Max = max(self.uCache, key=self.uCache.get)
            val = 1+ self.uCache[Max]
            self.uCache[key] += val
            
            return self.item[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.item:
            self.item[key] = value
            mru = max(self.uCache, key=self.uCache.get)
            a = self.uCache[mru] +1
            self.uCache[key] += a
        else:
            if len(self.item) < self.capacity:
                self.item[key] = value
                if self.uCache:
                    
                    mru = max(self.uCache, key=self.uCache.get)
                    
                    self.uCache[key] = 1 + self.uCache[mru]
                else:
                    self.uCache[key] = 1
                    self.Max = key
            else:
                lru = min(self.uCache, key=self.uCache.get)
                mru = max(self.uCache, key=self.uCache.get)
                a = self.uCache[mru]
            
                del self.item[lru]
                del self.uCache[lru]
                self.uCache[key] = 1 + a
                self.item[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)