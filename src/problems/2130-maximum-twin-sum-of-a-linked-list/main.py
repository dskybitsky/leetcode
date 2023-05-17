import sys
import os
from typing import Optional

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

from utils.list import ListNode, createList


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next.next

        while fast is not None:
            slow = slow.next
            fast = fast.next.next

        current = slow.next

        second_head = None

        while current is not None:
            next = current.next

            if second_head is None:
                second_head = current
                second_head.next = None
            else:
                current.next = second_head
                second_head = current
            
            current = next
        
        current_a = head
        current_b = second_head

        result = 0

        while current_b is not None:
            result = max(result, current_a.val + current_b.val)

            current_a = current_a.next
            current_b = current_b.next

        return result


sol = Solution()

assert sol.pairSum(createList([5, 4, 2, 1])) == 6
assert sol.pairSum(createList([4, 2, 2, 3])) == 7
assert sol.pairSum(createList([1, 100000])) == 100001
