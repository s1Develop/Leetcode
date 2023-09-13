"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 개멋있는 솔루션

        slow = fast = head

        # 대충 slow는 한 loop당 1번씩 가고 fast는 한 loop당 2번씩 가서 fast가 맨 끝에 다 다랐을때 slow가 간 length는 fast의 딱 절반이 되게 된다.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        