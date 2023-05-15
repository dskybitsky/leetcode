from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head

        i = 1

        while i < k:
            fast = fast.next
            i += 1

        first = fast

        slow = head

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        second = slow

        temp = first.val

        first.val = second.val

        second.val = temp

        return head


sol = Solution()

def listToListNode(vals: List[int])-> Optional[ListNode]:
    head = None
    tail = None

    for val in vals:
        if tail is None:
            tail = ListNode(val)
            head = tail
        else:
            tail.next = ListNode(val)
            tail = tail.next
    
    return head

def listNodeToList(head: Optional[ListNode]) -> List[int]:
    res = []
    curr = head

    while curr is not None:
        res.append(curr.val)
        curr = curr.next
    
    return res


assert listNodeToList(sol.swapNodes(listToListNode([1, 2, 3, 4, 5]), 2)) == [1, 4, 3, 2, 5]
assert listNodeToList(sol.swapNodes(listToListNode([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), 5)) == [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]
