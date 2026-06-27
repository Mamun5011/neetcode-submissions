# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if tree is empty, return depth 0
        if not root:
            return 0
        # use deque and start with root
        q = deque()
        q.append(root)
        depth = 0
        # pop the front and insert all of its child in each level and pop level wise
        while q:
            size = len(q)
            for i in range(size):
                front = q.popleft()
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            depth += 1
            
        return depth

        