# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # go through the both list and track list value and carry

        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            add = val1 + val2 + carry

            carry = add//10

            cur.next = ListNode(add%10)
            cur = cur.next
        return dummy.next

        
