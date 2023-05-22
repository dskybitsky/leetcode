from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = { }

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        index = [(k, v) for k,v in hash.items()]

        sorted_index = sorted(index, key = lambda x: x[1], reverse = True)

        result = []

        for i in range(k):
            result.append(sorted_index[i][0])

        return result


sol = Solution()

assert sol.topKFrequent([3,0,1,0], 1) == [0]
assert sol.topKFrequent([5, 2, 5, 3, 5, 3, 1, 1, 3], 2) == [5, 3]
assert sol.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert sol.topKFrequent([1], 1) == [1]
