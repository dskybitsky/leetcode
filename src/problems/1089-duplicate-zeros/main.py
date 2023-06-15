from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)

        shift = 0
        half_shift = 0
        i = 0

        while i < n - shift:
            if arr[i] == 0:
                if i < n - shift - 1:
                    shift += 1
                else:
                    half_shift = 1
            
            i += 1

        i = n - 1

        while i >= 0 and shift > 0:
            if arr[i - shift] == 0 and (i < n - 1 or half_shift == 1):
                arr[i - 1] = 0
                arr[i] = 0
                i -= 2
                shift -= 1
            else:
                arr[i] = arr[i - shift]
                i -= 1

sol = Solution()

arr1 = [1,0,2,3,0,4,5,0]

sol.duplicateZeros(arr1)

assert arr1 == [1,0,0,2,3,0,0,4]

arr2 = [8,4,5,0  ,0,  0,  0,  7]
sol.duplicateZeros(arr2)

assert arr2 == [8,4,5,0,0,0,0,0]
