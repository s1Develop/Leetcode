"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        #만약 현재 root에 아무것도 없으면 []를 return
        if root == None:
            return []
        
        #temp list를 만든다 to return
        temp = []
        
        # 만약 root의 left에 뭐가 있다면
        if root.left != None:
            #recursive call을 root.left로 부르면서 그거의 결과값을 temp에 더해준다
            temp = temp + self.inorderTraversal(root.left)

        # inorder traversal에서는 left->root->right순서대로 가니까 root의 val값을 temp에 넣어준다
        temp.append(root.val)

        # 만약 root의 right에 뭐가 있다면
        if root.right != None:

            #temp에다가 root.right을 recursive한 값을 넣어준다
            temp = temp + self.inorderTraversal(root.right)

        # 그리고 마지막에 temp를 return한다.
        return temp

