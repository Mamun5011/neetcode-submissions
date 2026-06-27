# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0

        def getDiameter(node):
            nonlocal res
            if not node:
                return 0
            left =  getDiameter(node.left)
            right = getDiameter(node.right)

            res = max(res, left+right)
            return max(left,right)+1
        getDiameter(root)
        return res
