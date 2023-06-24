from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # dp[taller - shorter] = taller
        dp = {0:0}
        
        for r in rods:
            # dp.copy() means we don't add r to these stands.
            new_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff
                
                # Add r to the taller stand, thus the height difference is increased to diff + r.
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)
                
                # Add r to the shorter stand, the height difference is expressed as abs(shorter + r - taller).
                new_diff = abs(shorter + r - taller)
                new_taller = max(shorter + r, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)
                
            dp = new_dp
            
        # Return the maximum height with 0 difference.
        return dp.get(0, 0)


sol = Solution()

#assert sol.tallestBillboard([2,4,8,16]) == 0
#assert sol.tallestBillboard([1,2,3,6]) == 6
assert sol.tallestBillboard([1,2,3,4,5,6]) == 10
assert sol.tallestBillboard([1,2]) == 0
