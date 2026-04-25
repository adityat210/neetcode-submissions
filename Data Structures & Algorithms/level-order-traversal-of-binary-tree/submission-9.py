# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs style approach
        #initialize the final returning array
        final = []
        #initialize the queue
        queue = collections.deque()
        queue.append(root)
        while queue:
            #keeps track of current level
            level = []
            #keeps track of length of previous level inserted
            qLen = len(queue)

            #for the length of that level and every node at that level, we want to add it to the level array
            for i in range(qLen):
                node = queue.popleft()
                #looking at the current level add the value of the node in that level
                if node:
                    level.append(node.val)
                #if that node has a left node then append that to the queue of nodes waiting to be discovered
                    if node.left:
                        queue.append(node.left)
                #if that node has a right node then append that to the queue of nodes waiting to be discovered
                    if node.right:
                        queue.append(node.right)

            #if the level array isn't empty, add that to the final array
            if level:
                final.append(level)

        return final
                
