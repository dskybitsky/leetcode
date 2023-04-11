from typing import List
from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        cand_dict = Counter(candidates)
        cand_keys = list(cand_dict.keys())

        def solve(i: int, accum: List[int], accum_dict: dict[int,int], target: int):
            if i == len(cand_keys):
                return

            cand_key = cand_keys[i]

            if target == 0:
                result.append(accum.copy())
                return

            if target < 0:
                return

            solve(i + 1, accum, accum_dict, target)

            if not cand_key in accum_dict:
                accum_dict[cand_key] = 0

            if accum_dict[cand_key] < cand_dict[cand_key]:
                accum.append(cand_key)
                accum_dict[cand_key] += 1
                solve(i, accum, accum_dict, target - cand_key)
                accum.pop()
                accum_dict[cand_key] -= 1

        accum = []
        accum_dict = {}

        solve(0, accum, accum_dict, target)

        return result

if __name__ == '__main__':
    sol = Solution()

    assert sol.combinationSum2([2,5,2,1,2], 5) == [
        [5],
        [2,2, 1],
    ]

    assert sol.combinationSum2([10,1,2,7,6,1,5], 8) == [
        [2,6],
        [1,7],
        [1,2,5],
        [1,1,6],
    ]