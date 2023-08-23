"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):

            # 즉 len가 0이어서 0 > -1일 경우
            if left > right:
                return None

            # even length이면 middle left의 index를 p로 잡고
            # odd length이면 딱 middle인 index를 p로 잡는다
            p = (left + right) // 2

            # root값을 nums[p] 즉 중간에 있는 애로 잡고
            root = TreeNode(nums[p])

            # preorder traversal로 즉 root -> left -> right 순서로 recursive한다

            # 그래서 left인 경우
            # 맨 왼쪽 index랑 p-1 index를 잡고 recursive를 하고
            root.left = helper(left, p-1)

            # right인 경우
            # 맨 오른쪽 index랑 p+1 index를 잡고 recursive를 한다
            root.right = helper(p + 1, right)

            # 그리고 마지막으로 root를 리턴함으로써 전체 TreeNode를 리턴한다
            return root

        # 맨 처음 시작을 맨 왼쪽 끝 index랑 맨 오른쪽 끝 index를 잡고 시작
        return helper(0, len(nums) - 1)

