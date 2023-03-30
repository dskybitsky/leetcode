import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

from structures.list import ListNode, printList, createList
from typing import Optional

class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        head = None
        tail = None

        current1 = list1
        current2 = list2

        while current1 != None or current2 != None:
            if current1 == None:
                nodeToAdd = current2
                current2 = current2.next
            elif current2 == None:
                nodeToAdd = current1
                current1 = current1.next
            elif current1.val < current2.val:
                nodeToAdd = current1
                current1 = current1.next
            else:
                nodeToAdd = current2
                current2 = current2.next
            
            if head == None:
                head = nodeToAdd
                tail = head
            else:
                tail.next = nodeToAdd
                tail = tail.next

        return head

if __name__ == "__main__":
    solution = Solution()

    newList = solution.mergeTwoLists(createList([1, 2, 4]), createList([1, 3, 4]))

    printList(newList)