# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            #change the values to 0 if no node at that place value
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # add the current values of the place together
            val = v1 + v2 + carry
            carry = val//10
            val = val % 10
            #place the next node as the current value calculated
            cur.next = ListNode(val)
            #updating the pointers 
            #go from cur to cur.next
            cur = cur.next
            #move l1 and l2 along too
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        #return the original cur value
        return dummy.next