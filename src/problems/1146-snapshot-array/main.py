import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.n = length
        self.data = { 0: { } }
        self.snapIndex = [[] for _ in range(length)]
        self.snapId = 0

        return

    def set(self, index: int, val: int) -> None:
        snapId = self.snapId

        self.data[snapId][index] = val

        self.snapIndex[index].append(self.snapId)

        return

    def snap(self) -> int:
        oldSnapId = self.snapId

        self.snapId += 1

        self.data[self.snapId] = { }

        return oldSnapId

    def get(self, index: int, snap_id: int) -> int:
        snapIds = self.snapIndex[index]

        snapIdPos = bisect.bisect(snapIds, snap_id) - 1

        if snapIdPos < 0:
            return 0

        snapId = snapIds[snapIdPos]

        if snapId not in self.data:
            return 0
        
        snap = self.data[snapId]

        if index not in snap:
            return 0
        
        return snap[index]
    
arr1 = SnapshotArray(3)

arr1.set(0,5)
assert arr1.snap() == 0
arr1.set(0,6)
assert arr1.get(0,0) == 5


arr2 = SnapshotArray(4)
assert arr2.snap() == 0
assert arr2.snap() == 1
assert arr2.get(3, 1) == 0
arr2.set(2, 4)
assert arr2.snap() == 2
arr2.set(1, 4)


arr3 = SnapshotArray(1)

arr3.set(0, 15)
assert arr3.snap() == 0
assert arr3.snap() == 1
assert arr3.snap() == 2
assert arr3.get(0, 2) == 15
assert arr3.snap() == 3
assert arr3.snap() == 4
assert arr3.get(0, 0) == 15

print("Ok")