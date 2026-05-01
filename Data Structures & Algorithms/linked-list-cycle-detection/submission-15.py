# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #keep track of visited nodes in a linkedList
        visited = set()
        #place the cur variable at the start of the List
        cur = head
        while cur:
            if cur in visited:
                return True
            #if not in visited add it
            visited.add(cur)
            #move the cur to the next
            cur = cur.next
        return False
        