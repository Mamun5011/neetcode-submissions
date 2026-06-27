# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root is empty then return null pointer
        if not root:
            return None
        # use a list and insert the root at first
        q = []
        q.append(root)
        # run a loop until the list is empty
        # in each iteration, pop the top and swap the left and right child 
        # after swapping, if the child is non empty, insert that into the list
        while q:
            top  = q.pop()
            temp  = top.left
            top.left = top.right
            top.right = temp

            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
        return root