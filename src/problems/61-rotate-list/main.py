import sys
import os
from typing import Optional

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

from utils.list import ListNode, createList, readList

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        fast = head

        length = 0

        while fast is not None:
            fast = fast.next
            length += 1
            
            if length == k:
                break

        if length < k:
            k = k % length

        fast = head
        
        for _ in range(k):
            fast = fast.next if fast.next is not None else head

        slow = head

        while fast.next is not None:
            slow = slow.next 
            fast = fast.next

        new_head = slow.next if slow.next is not None else head
        slow.next = None

        if fast != slow:
            fast.next = head
        
        return new_head
    
sol = Solution()

assert readList(sol.rotateRight(createList([]), 0)) == []
assert readList(sol.rotateRight(createList([1]), 0)) == [1]
assert readList(sol.rotateRight(createList([1, 2]), 0)) == [1, 2]
assert readList(sol.rotateRight(createList([1,2,3,4,5]), 2)) == [4,5,1,2,3]
assert readList(sol.rotateRight(createList([1,2,3,4,5]), 2)) == [4,5,1,2,3]

