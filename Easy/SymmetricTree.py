"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # 대충 여러개의 sub root를 계속 만드는 것
        return self.isMirror(root, root)


    def isMirror(self, t1, t2):

        # t1, t2 둘 다 아무것도 없다면 return True
        if not t1 and not t2:
            return True
        
        # 만약 t1, t2둘중 하나만 없다면 return False
        if not t1 or not t2:
            return False

        # t1이랑 t2값이 같고 recursive를 t1.right, t2.left랑 t1.left, t2.right들을 비교했을때 같은게 나온다면 return True
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
