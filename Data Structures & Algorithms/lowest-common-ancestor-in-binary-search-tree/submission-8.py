# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #initalize at root
        cur = root

        #while current is a valid node
        while cur:
            #if both values are less than the current value LCA should be on left
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            #if both values are more than current value LCA should be right
            elif p.val > cur.val and q.val > cur.val:
                return cur.right
            #should be currently at LCA
            else:
                return cur
