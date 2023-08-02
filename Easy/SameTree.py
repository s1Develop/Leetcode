"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # 만약 p랑 q 둘다 아무것도 없으면 True
        if not p and not q:
            return True
        
        # 만약 p랑 q중에 둘중 하나만 아무것도 없으면 False
        if not q or not p:
            return False
        
        # 만약 각 트리의 root값이 서로 다르다면 False
        if p.val != q.val:
            return False

        #이걸 양쪽 트리 right node들끼리 recursive한 결과랑 left node들끼리 recursive한 결과를 합친거를 리턴
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)