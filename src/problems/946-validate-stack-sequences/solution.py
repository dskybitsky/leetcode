from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        return False

if __name__ == '__main__':
    sol = Solution()

    assert sol.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]) == True
    assert sol.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]) == False