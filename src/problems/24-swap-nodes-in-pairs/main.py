import sys
import os
from typing import Optional

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

from utils.list import ListNode, createList, readList

class Solution:
    def swap(self, head: ListNode) -> ListNode:
        new_head = head.next
        tail = head.next.next

        new_head.next = head
        new_head.next.next = tail

        return new_head

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        current = head

        new_head = None
        tail = None
        
        while current is not None and current.next is not None:
            swapped = self.swap(current)

            if new_head is None:
                new_head = swapped

            if tail is not None:
                tail.next = swapped
            
            tail = swapped.next
            
            current = swapped.next.next

        return new_head

sol = Solution()

assert readList(sol.swapPairs(createList([1, 2, 3, 4]))) == [2, 1, 4, 3]
assert readList(sol.swapPairs(createList([]))) == []
assert readList(sol.swapPairs(createList([1]))) == [1]
