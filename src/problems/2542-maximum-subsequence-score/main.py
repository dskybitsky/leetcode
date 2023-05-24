from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])

        top_k_heap = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_heap)

        heapq.heapify(top_k_heap)

        ans = top_k_sum * pairs[k - 1][1]

        for i in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pairs[i][0]

            heapq.heappush(top_k_heap, pairs[i][0])

            ans = max(ans, top_k_sum * pairs[i][1])

        return ans


sol = Solution()

assert sol.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3) == 12
assert sol.maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1) == 30