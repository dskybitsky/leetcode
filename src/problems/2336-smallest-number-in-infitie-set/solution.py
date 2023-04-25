class SmallestInfiniteSet:

    def __init__(self):
        self._smallest = 1
        self._popped = set()

        return        

    def popSmallest(self) -> int:
        current = self._smallest

        next = self._smallest + 1

        while next in self._popped:
            next += 1

        self._smallest = next

        self._popped.add(current)

        return current

    def addBack(self, num: int) -> None:
        self._popped.discard(num)
        self._smallest = min(self._smallest, num)
        return


if __name__ == '__main__':
    sis = SmallestInfiniteSet()

    assert sis.popSmallest() == 1
    assert sis.popSmallest() == 2

    sis.addBack(1)
    sis.addBack(1)

    assert sis.popSmallest() == 1