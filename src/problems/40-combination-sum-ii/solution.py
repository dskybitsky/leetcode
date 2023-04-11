from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def solve(i: int, accum: List[int], target: int):
            if target == 0:
                result.append(accum.copy())
                return

            if target < 0:
                return

            if i == len(candidates):
                return

            solve(i + 1, accum, target)

            accum.append(candidates[i])

            solve(i + 1, accum, target - candidates[i])

            accum.pop()

        accum = []

        candidates.sort()

        solve(0, accum, target)

        return result

if __name__ == '__main__':
    sol = Solution()

    assert sol.combinationSum2([2,5,2,1,2], 5) == [
        [1,2,2],
        [5]
    ]

    assert sol.combinationSum2([10,1,2,7,6,1,5], 8) == [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
    ]