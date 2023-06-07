class FrequencyTracker:

    def __init__(self):
        self.vals = { }
        self.freqs = { }

    def add(self, number: int) -> None:
        if number in self.vals:
            self.vals[number] += 1
        else:
            self.vals[number] = 1

        freq = self.vals[number]

        self._addFreq(number, freq)

        if freq > 1:
            self._removeFreq(number, freq - 1)
        

    def deleteOne(self, number: int) -> None:
        if number not in self.vals:
            return
        
        self._removeFreq(number, self.vals[number])

        self.vals[number] -= 1

        if self.vals[number] == 0:
            self.vals.pop(number)
        
        if number in self.vals:
            self._addFreq(number, self.vals[number])


    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freqs
    

    def _addFreq(self, number: int, freq: int) -> int:
        if freq in self.freqs:
            self.freqs[freq].add(number)
        else:
            self.freqs[freq] = set([number])
    

    def _removeFreq(self, number: int, freq: int) -> int:
        self.freqs[freq].discard(number)

        if len(self.freqs[freq]) == 0:
            self.freqs.pop(freq)


frequencyTracker = FrequencyTracker()
frequencyTracker.add(3)
frequencyTracker.add(3)

assert frequencyTracker.hasFrequency(2) is True
assert frequencyTracker.hasFrequency(1) is False

frequencyTracker.deleteOne(2)

assert frequencyTracker.hasFrequency(2) is True
assert frequencyTracker.hasFrequency(1) is False

frequencyTracker.deleteOne(3)

assert frequencyTracker.hasFrequency(2) is False
assert frequencyTracker.hasFrequency(1) is True
