# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #need to keep track of two nodes, need one node to stay one behind and one node to stay one infront
        #could keep a counter variable, setting the length and then subtracting the nth value from that length as the expected return length and iterate through the linked list
        length = 0
        cur = head
        while cur:
            print(cur.val)
            length += 1
            cur = cur.next
        updated = length - n
        if updated == 0:
            return head.next
        cur = head
        for i in range(length - 1):
            if (i+1)==updated:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
