class LRUCache:

    def __init__(self, capacity: int):
        import collections
        self.capacity: int = capacity
        self.LRU: collections.OrderedDict = collections.OrderedDict()
    def get(self, key: int) -> int:
        value = self.LRU.get(key, -1)
        if value >= 0:
            self.LRU.update({key: self.LRU.pop(key)})
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == len(self.LRU):
            if key not in self.LRU:
                self.LRU.popitem(0)
                self.LRU.update({key: value})
            else:
                self.LRU.pop(key)
                self.LRU.update({key: value})
        else:
            if key in self.LRU:
                self.LRU.pop(key)
            self.LRU.update({key: value})


cache = LRUCache(2)
print(cache.put(2, 1))
print(cache.LRU.keys())
print(cache.put(1, 1))
print(cache.LRU.keys())
print(cache.put(2, 3))
print(cache.LRU.keys())
print(cache.put(4, 1))
print(cache.LRU.keys())
print(cache.get(1))
print(cache.get(2))
print(cache.get(3))
print(cache.get(4))

