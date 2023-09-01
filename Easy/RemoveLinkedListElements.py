"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        # 이렇게 하는 이유는 prev should always point to the node before the current head node,
        # and in the case where the first node in the list needs to be removed, 
        # the prev nodes should be pointing to the dummy node.
        prev = dummy
        # prev = ListNode()
        # prev.next = head

        while head != None:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next

        return dummy.next
        