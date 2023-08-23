"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional, List
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # reverse하게 숫자를 가져오기 위해서 먼저 str으로 바꾼다음 각 digit을 add해준다
        r1 = ''
        r2 = ''
        while l1 is not None or l2 is not None:
            if l1 is not None:
                r1 = str(l1.val) + r1
                l1 = l1.next
            if l2 is not None:
                r2 = str(l2.val) + r2
                l2 = l2.next

        # 그렇게 나온 str두개를 int로 바꾼 다음 더해준다
        result = int(r1) + int(r2)

        # 만약 그 값이 0이라면 그냥 0을 가진 linked-list를 리턴한다
        if result == 0:
            return ListNode(0)

        dummy = ListNode(0)
        current = dummy

        # first digit을 current노드의 val로 넣어준다
        while result != 0:
            current.next = ListNode(result % 10)
            current = current.next
            result = result // 10

        return dummy.next