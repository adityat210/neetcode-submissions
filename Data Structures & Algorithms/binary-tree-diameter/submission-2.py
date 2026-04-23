# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #longest path of the tree
        counter = 0

        def dfs(node):
            if not node:
                return 0
            nonlocal counter

            left = dfs(node.left)
            right = dfs(node.right)
            counter = max(counter, left+right)

            return 1 + max(left, right)
        dfs(root)
        return counter


