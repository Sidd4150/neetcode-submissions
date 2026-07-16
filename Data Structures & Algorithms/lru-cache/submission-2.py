class Node:
    def __init__(self,  key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None
    


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.size = 0   
        self.cache = {}

        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        

    
    def insert(self,node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right



    def get(self, key: int) -> int:

        if key in self.cache:
            #remove node and re add to right with new value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
        else:
            self.size += 1
            if self.cap < self.size:
                self.size -= 1
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)