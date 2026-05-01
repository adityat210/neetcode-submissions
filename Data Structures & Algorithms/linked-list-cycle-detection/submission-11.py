# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        explored = set()
        if head is None:
            return False
        temp = head
        while temp is not None:
            if temp in explored:
                return True
            explored.add(temp)
            temp = temp.next
        return False
