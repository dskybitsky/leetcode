import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
	def testSearchInsert(self):
		solution = Solution()
		
		self.assertEqual(2, solution.searchInsert([1,3,5,6], 5))
		self.assertEqual(1, solution.searchInsert([1,3,5,6], 2))
		
		self.assertEqual(0, solution.searchInsert([1, 2, 3], 0))
		self.assertEqual(0, solution.searchInsert([1, 2, 3], 1))
		self.assertEqual(1, solution.searchInsert([1, 2, 3], 2))
		self.assertEqual(2, solution.searchInsert([1, 2, 3], 3))
		self.assertEqual(3, solution.searchInsert([1, 2, 3], 4))
		
if __name__ == "__main__":
	unittest.main()
