# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #can do bfs style approach 
        #need to keep track of final result
        final = []

        q = collections.deque()
        q.append(root)

        while q:
            level = []
            lenQ = len(q)
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                final.append(level)
        return final

