from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(vals: List[int])-> Optional[ListNode]:
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

def readList(head: Optional[ListNode]) -> List[int]:
    res = []
    curr = head

    while curr is not None:
        res.append(curr.val)
        curr = curr.next
    
    return res

def printList(list: Optional[ListNode]):
    print('[', end = '')

    while list != None:
        template = "{val}, " if list.next != None else "{val}"
        print(template.format(val = list.val), end = '')
        list = list.next

    print(']')