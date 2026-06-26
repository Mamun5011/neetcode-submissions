# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy
        groupNext  = groupPrev.next

        while True:
            for i in range(k):
                if groupNext:
                    groupNext = groupNext.next
                else:
                    return dummy.next
            prev = groupNext
            cur = groupPrev.next

            while cur != groupNext:
                temp  = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            temp  = groupPrev.next
            groupPrev.next = prev
            groupPrev = temp
            groupNext = groupPrev.next
        return dummy.next