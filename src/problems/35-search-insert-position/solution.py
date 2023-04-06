from typing import List

class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		left = 0
		right = len(nums) - 1
		
		while left < right:			
			mid = left + (right - left) // 2
			
			if nums[mid] < target:
				left = mid + 1
			else:
				right = mid
				
		return left if nums[left] >= target else left + 1
		
		
if __name__ == "__main__":
	sol = Solution()

	print(sol.searchInsert([1,3,5,6], 5))

	print(sol.searchInsert([1, 2, 3], 0))	
	print(sol.searchInsert([1, 2, 3], 2))
	print(sol.searchInsert([1, 2, 3], 3))
	print(sol.searchInsert([1, 2, 3], 4))

