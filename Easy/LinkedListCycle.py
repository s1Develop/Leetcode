"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = {}
        dummy = head
        while dummy is not None:
            # 만약에 한번이라도 dump가 temp안에 있으면 return True 즉 cycle
            if dummy in temp:
                return True
            # temp의 key를 ListNode 자체 즉 dump로 넣어준다. 
            # 그래야 node의 val가 같다하더라고 각 고유의 node를 체크할 수 있기 때문에
            temp[dummy] = True
            dummy = dummy.next
        return False