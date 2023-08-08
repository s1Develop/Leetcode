"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # targetSum을 비교할때 recursive를 targetSum을 기준으로 root.val를 빼는걸로 시작

        # root가 처음부터 empty이면 False
        if not root:
            return False

        # root가 empty가 아니면 targetSum에 root.val를 뺀다
        targetSum -= root.val

        # root의 left랑 right가 empty이면
        # 이때 targetSum이 0인지 아닌지를 확인한다
        if root.left is None and root.right is None:
            return targetSum == 0

        # 그러고 recursive로 root.left랑 root.right을 하는데 거기에 targetSum은 항상 업데이트 된 애로 만들고 recursive한다.
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)