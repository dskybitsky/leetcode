from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)

        tail = -1
        current = 0

        def swap(i: int, j: int) -> None:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while current < n:
            if nums[current] == 0:
                current += 1
                continue

            if current == tail + 1:
                current += 1
                tail += 1
                continue
            
            swap(tail + 1, current)

            tail += 1
            current += 1

        return


sol = Solution()

nums1 = [0,1,0,3,12]

sol.moveZeroes(nums1)

assert nums1 == [1,3,12,0,0]

nums2 = [0]

sol.moveZeroes(nums2)

assert nums2 == [0]

nums3 = [1, 0, 1]

sol.moveZeroes(nums3)

assert nums3 == [1, 1, 0]