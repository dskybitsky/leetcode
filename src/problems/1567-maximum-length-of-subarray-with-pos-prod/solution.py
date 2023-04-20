from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def getMaxLenSub(nums: List[int], neg_count: int) -> int:
            n = len(nums)

            if neg_count % 2 == 0:
                return n
            
            if neg_count == 1:
                for i in range(n):
                    if nums[i] < 0:
                        return max(i, n - i - 1)
                
                return 0
            
            left_max = 0
            
            for i in range(n):
                if nums[i] < 0:
                    left_max = max(i, n - i - 1)
                    break

            right_max = 0

            for i in range(n - 1, -1, -1):
                if nums[i] < 0:
                    right_max = max(i, n - i - 1)
                    break

            return max(left_max, right_max)
        
        ans = 0
        n = len(nums)

        sub = []
        neg_count = 0

        for i in range(n):
            if nums[i] == 0:
                ans = max(ans, 0)

                if len(sub) > 0:
                    ans = max(ans, getMaxLenSub(sub, neg_count))
                    sub = []
                    neg_count = 0
            else:
                sub.append(nums[i])

                if nums[i] < 0:
                    neg_count += 1

        if len(sub) > 0:
            ans = max(ans, getMaxLenSub(sub, neg_count))

        return ans


if __name__ == '__main__':
    sol = Solution()

    assert sol.getMaxLen([1, -2, -3, 4]) == 4
    assert sol.getMaxLen([0, 1, -2, -3, -4]) == 3
    assert sol.getMaxLen([-1, -2, -3, 0, 1]) == 2
