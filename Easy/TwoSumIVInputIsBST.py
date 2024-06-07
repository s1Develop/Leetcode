"""
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
"""
from typing import Optional, Set
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        node_set = set()
        return self.helper(root, k, node_set)

    def helper(self, root: Optional[TreeNode], k: int, node_set: Set[int]) -> bool:
        if root == None:
            return False
        if k - root.val in node_set:
            return True
        
        node_set.add(root.val)
        return self.helper(root.left, k, node_set) or self.helper(root.right, k, node_set)
