import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.deque = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.deque:
            num = self.deque.pop(key)
            self.deque[key] = num
            return num
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.deque:
            self.deque.pop(key)
            self.deque[key] = value
        else:
            if self.cap>0:
                self.cap-=1
                self.deque[key] = value
            else:
                self.deque.popitem(last=False)
                self.deque[key]= value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)