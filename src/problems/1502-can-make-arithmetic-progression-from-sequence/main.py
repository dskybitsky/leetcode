from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)

        min_el = arr[0]
        max_el = arr[0]

        sum = 0

        for el in arr:
            sum += el
            min_el = min(min_el, el)
            max_el = max(max_el, el)

        index = set(arr)

        if len(index) != n:
            return min_el == max_el

        curr = min_el

        d = int((max_el - min_el) / (n - 1))

        for _ in range(1, n):
            curr += d

            if not curr in index:
                return False
        
        return True
    

sol = Solution()

assert sol.canMakeArithmeticProgression([3,5,1]) is True
assert sol.canMakeArithmeticProgression([1,2,4]) is False