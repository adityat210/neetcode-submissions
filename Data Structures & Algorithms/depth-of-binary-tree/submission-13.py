# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS version
        #initialize the stack
        if not root: 
            return 0
        stack = [[root, 1]]
        #iterate through the stack, adding only once the queue to val at every level
        result = 0
        while stack:
            node, val = stack.pop()
            if node:
                result = max(result, val)
                if node.right:
                    stack.append([node.right, val+1])
                if node.left:
                    stack.append([node.left, val+1])
        return result