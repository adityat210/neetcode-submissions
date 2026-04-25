# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #keep track of current node
        #utilize the property of bsts
            #left subtree going to have smaller values than root
            #right subtree going to have larger values than root
            #the first place where they have differing relativities to the roots is the place they'll diverge
        
        cur = root

        while cur: 
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
        