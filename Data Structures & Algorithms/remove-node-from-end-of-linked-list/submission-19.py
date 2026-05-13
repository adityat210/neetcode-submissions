# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #need to find length of the linked list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        #find the index you need to skip
        toRemove = length - n
        #if you need to remove the head node just return head.next
        if toRemove == 0:
            return head.next

        #setting cur = head and iterate through, skipping the one we want to remvoe and setting its previous pointer to the one after it
        cur = head
        for i in range(length-1):
            if (i+1) == toRemove:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
        