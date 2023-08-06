"""
Given a binary tree, determine if it is 
height-balanced.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true


Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def height(self, root:Optional[TreeNode]) -> int:
    # height(p) = -1 # if p is an empty subtree
    #            = 1 + max(height(p.left), height(p.right)) # otherwise

        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        #left의 height이랑 right의 height차이가 1이하이거나 isBalanced를 root.left랑 root.right을 둘 다해서 True가 나올 경우.
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

