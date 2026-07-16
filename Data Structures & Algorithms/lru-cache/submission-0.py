class LRUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict(tuple) # value, time
        self.capacity = capacity
        self.time = 0 
        self.size = 0 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.time += 1
            self.cache[key] = (self.cache[key][0],self.time  )
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        self.time +=1 
        if key in self.cache:
            self.cache[key] = (value,self.time)
        elif key not in self.cache:
            self.size +=1 

            if self.size > self.capacity:
                MIN = 1000000000000000000000
                delete = 0
                for key2 in self.cache:
                   
                    if self.cache[key2][1] < MIN:
                        delete = key2
                        MIN = self.cache[key2][1]
                self.cache.pop(delete)
                        

            self.cache[key] = (value,self.time)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)