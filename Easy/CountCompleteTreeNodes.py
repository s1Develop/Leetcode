"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
"""

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
complete binary tree: 대충 마지막 level을 제외한 나머지 level은 전부 filled in돼 있고
                        filled in안된 level에는 무조건 All the leaf elements must lean towards the left
                        complete binary tree does not have to be a fully binary tree (meaning that The last leaf element might not have a right sibling)
"""
from typing import Optional
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        temp = 0
        if root is None:
            return temp
        else:
            temp = 1 + self.countNodes(root.left) + self.countNodes(root.right)
        return temp