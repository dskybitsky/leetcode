from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)

        for num in nums1:
            s2.discard(num)
        
        for num in nums2:
            s1.discard(num)

        return [list(s1), list(s2)]
    

if __name__ == "__main__":
    sol = Solution()

    assert sol.findDifference([1, 2, 3], [2, 4, 6]) == [[1, 3], [4, 6]]
