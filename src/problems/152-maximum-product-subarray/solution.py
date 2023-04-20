from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.MIN = -20001

        def productSub(nums: List[int], left, right) -> int:
            prod = nums[left]

            for i in range(left + 1, right + 1):
                prod *= nums[i]

            return prod

        def maxProductSub(nums: List[int], neg_count: int) -> int:
            n = len(nums)

            if neg_count % 2 == 0:
                return productSub(nums, 0, n - 1)
            
            if neg_count == 1:
                for i in range(n):
                    if nums[i] < 0:
                        return max(
                            productSub(nums, 0, i - 1) if i > 0 else self.MIN, 
                            nums[i], 
                            productSub(nums, i + 1, n - 1) if i < n -1 else self.MIN
                        )
                
                return self.MIN
            
            left_max = self.MIN
            
            for i in range(n):
                if nums[i] < 0:
                    left_max = max(
                        productSub(nums, 0, i - 1) if i > 0 else self.MIN, 
                        nums[i],
                        productSub(nums, i + 1, n - 1) if i < n -1 else self.MIN
                    )
                    break

            right_max = self.MIN

            for i in range(n - 1, -1, -1):
                if nums[i] < 0:
                    right_max = max(
                        productSub(nums, 0, i - 1) if i > 0 else self.MIN, 
                        nums[i],
                        productSub(nums, i + 1, n - 1) if i < n -1 else self.MIN
                    )
                    break

            return max(left_max, right_max)
        
        ans = self.MIN
        n = len(nums)

        sub = []
        neg_count = 0

        for i in range(n):
            if nums[i] == 0:
                ans = max(ans, 0)

                if len(sub) > 0:
                    ans = max(ans, maxProductSub(sub, neg_count))
                    sub = []
                    neg_count = 0
            else:
                sub.append(nums[i])

                if nums[i] < 0:
                    neg_count += 1

        if len(sub) > 0:
            ans = max(ans, maxProductSub(sub, neg_count))

        return ans


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxProduct([0, 2]) == 2
    assert sol.maxProduct([2, -5, -2, -4, 3]) == 24
    assert sol.maxProduct([-2, -3, 7]) == 42
    assert sol.maxProduct([3, -1, 4]) == 4
    assert sol.maxProduct([-2]) == -2
    assert sol.maxProduct([2, 3, -2, 4]) == 6
    assert sol.maxProduct([-2, 0, -1]) == 0
