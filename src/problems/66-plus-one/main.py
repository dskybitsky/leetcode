from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        digits.insert(0, 1)

        return digits


sol = Solution()

assert sol.plusOne(digits = [1,2,3]) == [1, 2, 4]
assert sol.plusOne(digits = [9]) == [1, 0]