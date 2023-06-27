import sys
import os
from typing import Optional

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

from utils.list import ListNode, createList, readList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        current = head

        while current is not None:
            while current.next is not None and current.next.val == current.val:
                current.next = current.next.next
            
            current = current.next

        return head


sol = Solution()

assert readList(sol.deleteDuplicates(createList([1,1,2]))) == [1,2]
assert readList(sol.deleteDuplicates(createList([1,1,2,3,3]))) == [1,2,3]