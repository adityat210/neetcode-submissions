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

        #using dfs
        def dfs(root):
            nonlocal counter
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            counter = max(counter, right+left)
            return 1 + max(right, left)
        
        dfs(root)
        return counter

