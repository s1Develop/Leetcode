"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # empty이면 그대로 head 리턴
        if head == None:
            return head

        # current라는 애를 head의 next애로 잡고 prev를 head자체로 잡는다
        current = head.next
        prev = head

        while current != None:
            #그래서 current자체가 prev 즉 그전애의 값이랑 같으면
            if current.val == prev.val:
                
                # 전 애의 next는 current의 next가 된다. 즉 current을 없애버리는 것 (중복 숫자이기 때문에)
                prev.next = current.next

                # 그리고 current를 없애고 그 자리를 current.next가 차지하게 된다
                current = current.next
            
            # current자제가 prev 즉 그전애의 값이랑 다르다면
            else:
                # current를 current.next로 만들어서 다음 loop로 갈 수 있게 만들고
                current = current.next

                # current랑 같이 prev를 prev.next로 만들어서 다음 loop로 갈 수 있게 만든다.
                prev = prev.next
        
        # 마지막에 head 즉 맨 처음 노드를 리턴하기
        return head