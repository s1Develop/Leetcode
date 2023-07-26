"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:
list1: 1->2->4
list2: 1->3->4
result: 1->1->2->3->4->4

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
from typing import List

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # 두개의 linked list (그래서 두개 다 같은 linked list의 head를 포인트하도록 설정)
        ranNode = dummy = ListNode()
        while list1 and list2:

            #만약 list2의 값이 list1의 값보다 크면 ranNode의 next node가 list1이 되도록하고
            # 그 ranNode는 list1이 되도록하면서
            # list1자체는 list1.next가 되도록만든다
            if list1.val < list2.val:
                ranNode.next = list1
                #list1, ranNode = list1.next, list1 밑에 두줄이랑 같은 뜻
                ranNode = list1
                list1 = list1.next

            #만약 list2의 값이 list1의 값보다 작거나 같으면 ranNode의 next node가 list2이 되도록하고
            # 그 ranNode는 list2이 되도록하면서
            # list2자체는 list2.next가 되도록만든다
            else:
                ranNode.next = list2
                #list2, ranNode = list2.next, list2 밑에 두줄이랑 같은 뜻
                ranNode = list2
                list2 = list2.next
        
        #대충 while loop이 끝나고 list1이랑 list2둘중하나에 아직 더 남아 있을 경우
        #list1이 남아있으면 ranNode의 next를 list1로 잡고
        if list1:
            ranNode.next = list1
        #list2이 남아있으면 ranNode의 next를 list2로 잡는다.
        else:
            ranNode.next = list2

        #마지막으로 ranNode의 맨처음 시작node를 가르켰던 dummy의 next를 return하게 된다
        #dummy.next를 하는 이유는 dummy자체는 값을 안가지고 있고 point만 하고 있기 때문에.
        return dummy.next
        
