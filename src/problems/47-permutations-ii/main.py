from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def permute(offset: int = 0) -> List[List[int]]:
            if offset == n:
                return []
            
            if offset == n - 1:
                return [[nums[offset]]]
            
            res = []

            permutes_index = set()

            next_permutes = permute(offset + 1)

            for i in range(len(next_permutes)):
                for j in range(len(next_permutes[i]) + 1):
                    num = nums[offset]

                    res_item = next_permutes[i][:j] + [num] + next_permutes[i][j:]

                    res_item_t = tuple(res_item)

                    if res_item_t not in permutes_index:
                        res.append(res_item)
                        permutes_index.add(res_item_t)

            return res
        
        res = permute()

        return res


sol = Solution()

assert sorted(sol.permuteUnique([1,2,3])) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
assert sorted(sol.permuteUnique([1,1,2])) == sorted([[1,1,2],[1,2,1],[2,1,1]])
