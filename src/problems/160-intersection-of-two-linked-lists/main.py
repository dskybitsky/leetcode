from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        curr_a = head_a
        len_a = 1

        while curr_a is not None:
            curr_a = curr_a.next
            len_a += 1

        curr_b = head_b
        len_b = 1

        while curr_b is not None:
            curr_b = curr_b.next
            len_b += 1

        curr_a = head_a
        curr_b = head_b

        if len_a > len_b:
            offset = len_a - len_b

            for _ in range(offset):
                curr_a = curr_a.next
        elif len_b > len_a:
            offset = len_b - len_a

            for _ in range(offset):
                curr_b = curr_b.next
        
        while curr_a is not None and curr_b is not None:
            if curr_a == curr_b:
                return curr_a
            
            curr_a = curr_a.next
            curr_b = curr_b.next
        
        return None