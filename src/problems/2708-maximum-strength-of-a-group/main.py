from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)

        pos_prod = 0
        neg_prod = 0
        neg_max = -10
        neg_count = 0
        zero_count = 0

        for i in range(n):
            num = nums[i]

            if num > 0:
                pos_prod = num if pos_prod == 0 else pos_prod * num
            elif num < 0:
                neg_prod = num if neg_prod == 0 else neg_prod * num
                neg_max = max(neg_max, num)
                neg_count += 1
            else:
                zero_count += 1

        res = None

        if pos_prod > 0:
            res = pos_prod if res is None else res * pos_prod
        
        if neg_count > 1:
            neg_prod_pos = neg_prod if neg_prod > 0 else int(neg_prod / neg_max)
            res = neg_prod_pos if res is None else res * neg_prod_pos

        if res is None:
            return 0 if zero_count > 0 else neg_prod
        
        return res


sol = Solution()

assert sol.maxStrength([3,-1,-5,2,5,-9]) == 1350
assert sol.maxStrength([-4,-5,-4]) == 20
assert sol.maxStrength([0,-1]) == 0
assert sol.maxStrength([-9]) == -9
