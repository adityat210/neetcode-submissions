# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #could do a bst style approach, while the queue isn't empty keep popping, adding to the array
        res = []
        q = collections.deque()

        q.append(root)

        while q:
            lenQ = len(q)
            level = []
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
