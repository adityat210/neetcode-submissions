# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS version
        stack = [[root, 1]]
        if not root:
            return 0
        result = 0
        while stack:
            node, val = stack.pop()
            if node:
                result = max(val, result)
                stack.append([node.right, val+1])
                stack.append([node.left, val+1])

        return result

