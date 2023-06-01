from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity # initialise the capacity of the cache
        self.m = dict() # initialise the dictionary
        self.deq = deque() # initialise the deque
        
    def get(self, key: int) -> int:
        if(key in self.m):
            value = self.m[key] 
            self.deq.remove(key) # remove the key from the cache
            self.deq.append(key) # append to top of cache
            return value 
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(key not in self.m):
            if(len(self.deq) == self.c):
                oldest = self.deq.popleft() # remove and return leftmost element
                del self.m[oldest] # delete the item
        else:
            self.deq.remove(key) # remove the key
        self.m[key] = value # assign the key a value in the dictionary
        self.deq.append(key) # append the key to the cache
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
