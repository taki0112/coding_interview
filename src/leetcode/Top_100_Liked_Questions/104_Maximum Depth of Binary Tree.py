# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode, depth=0) -> int:
        if root == None:
            return depth

        x = max(self.maxDepth(root.left, depth + 1), self.maxDepth(root.right, depth + 1))

        return x
