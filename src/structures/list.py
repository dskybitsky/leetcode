from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(vals): 
    head = None
    tail = None

    for i in vals:
        if head == None:
            head = ListNode(i)
            tail = head
        else:
            tail.next = ListNode(i)
            tail = tail.next
    
    return head

def printList(list: Optional[ListNode]):
    print('[', end = '')

    while list != None:
        template = "{val}, " if list.next != None else "{val}"
        print(template.format(val = list.val), end = '')
        list = list.next

    print(']')