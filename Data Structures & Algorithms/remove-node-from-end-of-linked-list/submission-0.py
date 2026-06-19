# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # set the two pointer and move second pointer n times
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = head
        for i in range(n):
            fast = fast.next
        
        # move both pointer together until 2nd pointer is not null

        while fast:
            slow = slow.next
            fast = fast.next
        # remove the node after first pointer
        slow.next = slow.next.next
        return dummy.next
