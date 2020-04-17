# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Left -> Root -> Right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        x = []
        self.solver(root, x)
        return x

    def solver(self, root, x):
        if root:
            self.solver(root.left, x)
            x.append(root.val)
            self.solver(root.right, x)


