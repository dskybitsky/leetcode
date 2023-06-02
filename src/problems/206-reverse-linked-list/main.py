import sys
import os
from typing import Optional

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

from utils.list import ListNode, createList, readList


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None

        current = head

        while current is not None:
            next = current.next

            current.next = new_head

            new_head = current

            current = next

        return new_head
    

sol = Solution()

assert readList(sol.reverseList(createList([1,2,3,4,5]))) == [5,4,3,2,1]