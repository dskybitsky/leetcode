class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        if x == 1:
            return 1

        while (right - left) > 1:
            mid = left + (right - left) // 2

            if mid * mid > x:
                right = mid
            elif mid * mid < x:
                left = mid
            else:
                return mid
            
        return left


sol = Solution()


assert sol.mySqrt(0) == 0
assert sol.mySqrt(1) == 1
assert sol.mySqrt(4) == 2
assert sol.mySqrt(8) == 2
