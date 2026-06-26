# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # set group Previous pointer
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy
        groupNext  = groupPrev.next

        while True:
            # fix the groupNext after K groups
            for i in range(k):
                if groupNext:
                    groupNext = groupNext.next
                else:
                    return dummy.next
            # set the prev and cur to reverse the current k group    
            prev = groupNext
            cur = groupPrev.next

            while cur != groupNext:
                temp  = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            # connect group Prev with the current reversed chain
            temp  = groupPrev.next
            groupPrev.next = prev
            groupPrev = temp
       
        return dummy.next