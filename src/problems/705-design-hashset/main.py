class MyHashSet:

    def __init__(self):
        self.maxSlots = 65536
        self.buckets = [None] * self.maxSlots

    def add(self, key: int) -> None:
        bucketId = key % self.maxSlots

        if self.buckets[bucketId] is None:
            self.buckets[bucketId] = []

        for i in range(len(self.buckets[bucketId])):
            if key == self.buckets[bucketId][i]:
                return
        
        self.buckets[bucketId].append(key)
        

    def remove(self, key: int) -> None:
        bucketId = key % self.maxSlots

        if self.buckets[bucketId] is None:
            return
        
        for i in range(len(self.buckets[bucketId])):
            if key == self.buckets[bucketId][i]:
                self.buckets[bucketId].pop(i)
                return
        

    def contains(self, key: int) -> bool:
        bucketId = key % self.maxSlots

        if self.buckets[bucketId] is None:
            return False
        
        for i in range(len(self.buckets[bucketId])):
            if key == self.buckets[bucketId][i]:
                return True
        
        return False
    
myHash = MyHashSet()

myHash.add(1)
myHash.add(2)

assert myHash.contains(1)
assert myHash.contains(3) is False

myHash.add(2)

assert myHash.contains(2)

myHash.remove(2)

assert myHash.contains(2) is False