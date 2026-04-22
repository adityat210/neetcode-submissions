# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)
        
        #counter to keep track of level
        count = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.right: 
                    q.append(node.right)
                if node.left: 
                    q.append(node.left)

            count += 1

        return count

