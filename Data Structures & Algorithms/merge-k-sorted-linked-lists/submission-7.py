# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # get two lists and merge correspondingly to make a single list
   
        length = len(lists)

        if length == 0:
            return None

        

        while length != 1:
            res = []
            for i in range(0,length,2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < length else None
                mergeList  = self.merge(l1,l2)
                res.append(mergeList)
            lists  = res
            length = len(lists)
            #print(length)
        return lists[0]


    def merge(self,l1,l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next








        # merge two list
        