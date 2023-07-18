from typing import Optional

class CacheListNode:
    def __init__(self, key: int, val: int, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

        return        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        
        self._bump(node)
        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._bump(node)
            return
        
        added = CacheListNode(key, value)

        self.map[key] = added
        
        self._push(added)

        if len(self.map) > self.capacity:
            evicted = self._pop()

            del self.map[evicted.key]
    
    def _bump(self, node: CacheListNode) -> None:
        # Head
        if node.prev is None:
            return
        
        # Tail
        if node.next is None:
            self._pop()
            self._push(node)

            return

        # Middle
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self._push(node)

    def _push(self, node: CacheListNode) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.head.prev = node
        node.prev = None
        node.next = self.head
        self.head = node

    def _pop(self) -> CacheListNode:
        node = self.tail
        
        self.tail = node.prev
        self.tail.next = None

        if self.tail.prev is None:
            self.tail.prev = self.head

        return node

lRUCache = LRUCache(2)

lRUCache.put(2,1)
lRUCache.put(2,2)

assert lRUCache.get(2) == 2

lRUCache.put(1,1)
lRUCache.put(4,1)

assert lRUCache.get(2) == -1


lRUCache = LRUCache(3)

lRUCache.put(1,1)
lRUCache.put(2,2)
lRUCache.put(3,3)
lRUCache.put(4,4)

assert lRUCache.get(4) == 4
assert lRUCache.get(3) == 3
assert lRUCache.get(2) == 2
assert lRUCache.get(1) == -1

lRUCache.put(5,5)

assert lRUCache.get(1) == -1
assert lRUCache.get(2) == 2
assert lRUCache.get(3) == 3
assert lRUCache.get(4) == -1
assert lRUCache.get(5) == 5



lRUCache = LRUCache(2)

lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}

assert lRUCache.get(1) == 1    # return 1

lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}

assert lRUCache.get(2) == -1   # returns -1 (not found)

lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}

assert lRUCache.get(1) == -1   # return -1 (not found)
assert lRUCache.get(3) == 3    # return 3
assert lRUCache.get(4) == 4    # return 4
